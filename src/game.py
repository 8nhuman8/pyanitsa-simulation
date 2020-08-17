from randword import name

from deck import Deck
from player import Player


class Game:
    def __init__(self, players_amount: int):
        self.players_amount = players_amount
        self.players = [Player(name()) for _ in range(self.players_amount)]

        self.deck = Deck()
        self._equalize_deck()

        self._hand_out_deck()


    def _equalize_deck(self):
        deck_cards_amount = len(self.deck)
        stop_value = deck_cards_amount - deck_cards_amount % self.players_amount
        self.deck.cards = self.deck.cards[slice(None, stop_value)]


    def _hand_out_deck(self):
        hand_cards_amount = len(self.deck) // self.players_amount
        for player in self.players:
            for _ in range(hand_cards_amount):
                player.draw(self.deck)
