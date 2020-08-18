from random import shuffle as rand_shuffle

from card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self._build()
        self._shuffle()

    def __len__(self) -> int:
        return len(self.cards)

    def show(self) -> None:
        print(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def _build(self) -> None:
        suits = ('\u2660', '\u2666', '\u2663', '\u2665') # ≡ ('♠', '♦', '♣', '♥')
        self.cards = [Card(value, suit) for value in range(2, 15) for suit in suits]

    def _shuffle(self) -> None:
        rand_shuffle(self.cards)
