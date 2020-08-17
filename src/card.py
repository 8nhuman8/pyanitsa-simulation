from dataclasses import dataclass


@dataclass
class Card:
    value: int
    suit: str

    def __str__(self):
        return f'{self.value} of {self.suit}'

    def __repr__(self):
        return f'Card({self.value}, {self.suit})'
