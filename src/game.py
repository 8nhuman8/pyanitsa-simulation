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


    def main_loop(self) -> None:
        while any([player.hand for player in self.players]):
            cards = {player.name: player.put() for player in self.players}
            #max_card = max(cards.values())
            #dispute_cards = OrderedDict({name: card for name, card in cards.items() if card == max_card})
            #if len(dispute_cards) == 1:
            #    dispute_cards[max_card].take(cards)
            #dispute_cards[max_card].show_hand()
            #print(dispute_cards.items()[0])
            input()
