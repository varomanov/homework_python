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


cards = [Card(value, suit) for suit in SUITS for value in VALUES]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

# TODO-2: Выведите карты в формате: cards[кол-во]2♠, 3♠, 4♠ ... A♠, ..., 2♦, 3♦ ... A♦, 2♥, 3♥, 4♥ ... A♥
print(f'cards[{len(cards)}]', *[x.to_str() for x in cards])
