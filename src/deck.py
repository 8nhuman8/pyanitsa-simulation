from random import shuffle as rand_shuffle

from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self._build()
        self._shuffle()

    def __len__(self):
        return len(self.cards)

    def show(self):
        print(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def _build(self):
        suits = ('\u2660', '\u2666', '\u2663', '\u2665')    # === ('♠', '♦', '♣', '♥')
        self.cards = [Card(value, suit) for value in range(1, 14) for suit in suits]

    def _shuffle(self):
        rand_shuffle(self.cards)
