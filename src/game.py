from collections import OrderedDict

from randword import name

from deck import Deck
from player import Player


class Game:
    def __init__(self, players_amount: int) -> None:
        self.players_amount = players_amount
        self.players = [Player(name()) for _ in range(self.players_amount)]

        self.deck = Deck()
        self.__equalize_deck()

        self.__hand_out_deck()


    def show_players_hands(self):
        for player in self.players:
            print(player.name, end=': ')
            print(player.hand, end='\n\n')


    def __equalize_deck(self) -> None:
        deck_cards_amount = len(self.deck)
        stop_value = deck_cards_amount - deck_cards_amount % self.players_amount
        self.deck.cards = self.deck.cards[slice(None, stop_value)]


    def __hand_out_deck(self) -> None:
        hand_cards_amount = len(self.deck) // self.players_amount
        for player in self.players:
            for _ in range(hand_cards_amount):
                player.draw(self.deck)


    def __find_player(self, name: str) -> Player:
        return next(player for player in self.players if player.name == name)


    def __dispute_process(self, cards: list) -> None:
        max_card = max(cards)
        dispute_cards = [card for card in cards if card == max_card]

        if len(dispute_cards) == 1:
            max_card_owner = max_card.owner
            self.__find_player(max_card_owner).take(cards)
            self.__find_player(max_card.owner).show_hand()
        else:
            pass


    def main_loop(self) -> None:
        while any([player.hand for player in self.players]):
            cards = [player.put() for player in self.players]
            self.__dispute_process(cards)
            input()
