from deck import Deck
from card import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []

    def __str__(self) -> str:
        return f'Player {self.name}'

    def __repr__(self) -> str:
        return f'Player({self.name})'

    def show_hand(self) -> None:
        print(f'{self.name}\'s total amount of cards: {len(self.hand)}')
        for card in self.hand[:-1]:
            print(card, end=', ')
        if self.hand:
            print(self.hand[-1])
        print(end='\n')

    def draw(self, deck: Deck) -> None:
        card = deck.draw_card()
        card.owner = self.name
        self.hand.append(card)

    def take(self, cards: list[Card]) -> None:
        for card in cards:
            card.owner = self.name
        self.hand = cards + self.hand

    def put(self) -> Card:
        return self.hand.pop()
