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


    def __show_players_hands(self) -> None:
        print('START --------------------------------------------', end='\n\n')
        for player in self.players:
            player.show_hand()
        print('END ----------------------------------------------', end='\n\n')


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


    def __is_over(self) -> bool:
        return sum([int(bool(player.hand)) for player in self.players]) == 1


    def __dispute_process(self, cards: list, closed_cards: list) -> None:
        max_card = max(cards)
        dispute_cards = [card for card in cards if card == max_card]
        print('Dispute cards:', cards, end='\n\n')

        if len(dispute_cards) == 1:
            max_card_owner = max_card.owner
            print(cards + closed_cards)
            self.__find_player(max_card_owner).take(cards + closed_cards)
            self.__find_player(max_card_owner).show_hand()
        else:
            players_in_dispute = [self.__find_player(card.owner) for card in dispute_cards]
            print(players_in_dispute)
            cl = cards + [player.put() for player in players_in_dispute]
            c = [player.put() for player in players_in_dispute]
            self.__dispute_process(c, cl)



    def main_loop(self) -> None:
        while not self.__is_over():
            self.__show_players_hands()
            cards = [player.put() for player in self.players if player.hand]
            self.__dispute_process(cards, [])
        self.__show_players_hands()
