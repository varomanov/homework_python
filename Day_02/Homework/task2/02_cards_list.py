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


hearts_cards = [Card(value, 'Hearts') for value in VALUES]
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = [Card(value, 'Diamonds') for value in VALUES]
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(*[card.to_str() for card in hearts_cards], sep=', ')
