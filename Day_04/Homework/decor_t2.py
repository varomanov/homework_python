"""
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях
либо в доллары (курс: 1$ = 99 рублей)
либо в евро (курс: 1€ = 102 рубля)
либо в юани (курс: 1¥ = 14 рублей)
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
chr(165) -> '¥'

before decorating: 10000₽
after: 100€
"""
exchange = {
    'USD': 99,
    'EUR': 102,
    'CNY': 14,
}

currency_symbols = {
    'USD': chr(36),  # '$'
    'EUR': chr(8364),  # '€'
    'CNY': chr(165),  # '¥'
    'RUB': chr(8381)  # '₽'
}


def main(currency):
    def converter(func):
        def wrapper(*args, **kwargs):
            # Вызываем оригинальную функцию и получаем результат в рублях
            result_rub = func(*args, **kwargs)

            # Извлекаем числовое значение из строки (убираем символ ₽)
            rub_amount = float(result_rub.replace('₽', ''))

            # Конвертируем в выбранную валюту
            rate = exchange[currency.upper()]
            converted_amount = rub_amount / rate

            # Получаем символ валюты
            symbol = currency_symbols[currency.upper()]

            return f'{round(converted_amount, 2)}{symbol}'

        return wrapper

    return converter


@main(currency='usd')
def summa(count: float, price: float) -> str:
    """ Out: <float><CHAR>"""
    return f'{round(count * price, 2)}₽'


# Тестирование
print(summa(305.5, 2.4))  # 305.5 * 2.4 = 733.2₽ -> 733.2 / 99 ≈ 7.41$
print(summa(1000, price=10))  # 1000 * 10 = 10000₽ -> 10000 / 99 ≈ 101.01$