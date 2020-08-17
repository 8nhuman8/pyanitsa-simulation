from deck import Deck


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def __str__(self):
        return f'Player {self.name}'

    def __repr__(self):
        return f'Player({self.name})'

    def show_hand(self):
        print(f'Total amount of cards: {len(self.hand)}')
        for card in self.hand:
            print(card)

    def draw(self, deck: Deck):
        self.hand.append(deck.draw_card())
