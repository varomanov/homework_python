import json
import requests
from functools import total_ordering


@total_ordering
class Money:
    def __init__(self, rubles=0, kopecks=0):
        # Преобразуем все в копейки для удобства вычислений
        total_kopecks = rubles * 100 + kopecks
        self.rubles = total_kopecks // 100
        self.kopecks = total_kopecks % 100

    def _normalize(self):
        """Приводит сумму к нормальному виду (копейки <= 99)"""
        total_kopecks = self.rubles * 100 + self.kopecks
        self.rubles = total_kopecks // 100
        self.kopecks = total_kopecks % 100
        return self

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        total_kopecks = (self.rubles + other.rubles) * 100 + (self.kopecks + other.kopecks)
        return Money(0, total_kopecks)._normalize()

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        total_kopecks = (self.rubles - other.rubles) * 100 + (self.kopecks - other.kopecks)
        return Money(0, total_kopecks)._normalize()

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        total_kopecks = (self.rubles * 100 + self.kopecks) * other
        return Money(0, total_kopecks)._normalize()

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.rubles == other.rubles and self.kopecks == other.kopecks

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self_total = self.rubles * 100 + self.kopecks
        other_total = other.rubles * 100 + other.kopecks
        return self_total < other_total

    def __mod__(self, percentage):
        """Вычисление процента от суммы"""
        if not isinstance(percentage, (int, float)):
            return NotImplemented

        total_kopecks = self.rubles * 100 + self.kopecks
        percent_kopecks = round(total_kopecks * percentage / 100)
        return Money(0, percent_kopecks)._normalize()

    def convert(self, currency_code):
        """Конвертация валюты с использованием актуального курса"""
        try:
            url = 'https://www.cbr-xml-daily.ru/daily_json.js'
            response = requests.get(url)
            response.raise_for_status()

            data_dict = json.loads(response.text)

            if currency_code.upper() not in data_dict['Valute']:
                raise ValueError(f"Валюта {currency_code} не найдена")

            rate = data_dict['Valute'][currency_code.upper()]['Value']
            nominal = data_dict['Valute'][currency_code.upper()]['Nominal']

            # Конвертируем рубли в целевую валюту
            total_rubles = self.rubles + self.kopecks / 100
            converted_amount = total_rubles / rate * nominal

            return converted_amount

        except requests.RequestException:
            # Fallback на статические курсы если нет интернета
            static_rates = {
                'USD': 99.0,
                'EUR': 102.0,
                'CNY': 14.0
            }

            if currency_code.upper() not in static_rates:
                raise ValueError(f"Валюта {currency_code} не поддерживается")

            rate = static_rates[currency_code.upper()]
            total_rubles = self.rubles + self.kopecks / 100
            converted_amount = total_rubles / rate

            return converted_amount

    def __str__(self):
        self._normalize()
        kopecks_str = f"{self.kopecks:02d}"  # Форматируем копейки с ведущим нулем
        return f"{self.rubles}руб {kopecks_str}коп"

    def __repr__(self):
        return f"Money({self.rubles}, {self.kopecks})"


# Примеры использования
if __name__ == "__main__":
    # Создаем сумму из 20 рублей и 120 копеек
    money1 = Money(20, 120)
    print(money1)  # 21руб 20коп

    # Создаем две денежные суммы
    money1 = Money(20, 60)
    money2 = Money(10, 45)

    # Складываем суммы
    money3 = money1 + money2
    print(money3)  # 31руб 05коп

    # Вычитание
    money4 = money1 - money2
    print(money4)  # 10руб 15коп

    # Умножение на целое число
    money5 = money1 * 3
    print(money5)  # 61руб 80коп

    # Сравнение
    print(money1 > money2)  # True
    print(money1 == Money(20, 60))  # True

    # Процент от суммы
    money6 = money1 % 20
    print(money6)  # 4руб 12коп

    # Конвертация валют (требует интернет-соединения)
    try:
        usd_amount = money1.convert("USD")
        print(f"{money1} = {usd_amount:.2f} USD")
    except Exception as e:
        print(f"Ошибка конвертации: {e}")