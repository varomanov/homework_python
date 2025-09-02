# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
    'Spades': '♠',
    'Clubs': '♣',
    'Diamonds': '♦',
    'Hearts': '♥'
}


class Card:
    def __init__(self, value: str, suit: str):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

    def to_str(self):
        return ''.join([self.value, SUITS_UNI[self.suit]])

    def equal_suit(self, other_card):
        return other_card.suit == self.suit

    def more(self, other_card):
        return self.value > other_card.value

    def less(self, other_card):
        return self.value < other_card.value


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())


# Проверим, одинаковые ли масти у карт
# if card1.equal_suit(card2):
#     print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
# else:
#     print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

# print('\u2661', '\u2665')
# print('\u2662', '\u2666')
# print('\u2667', '\u2663')
# print('\u2664', '\u2660')
