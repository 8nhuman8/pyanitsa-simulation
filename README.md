# Pyanitsa Simulation

The simulation of a Russian card game «Пьяница» ("P'yanitsa"), a.k.a. "War" in the USA, a.k.a. "Battle" in the UK

## Table of contents

- [Information about the game](#information-about-the-game)
  - [Rules](#rules)
  - [Dispute](#dispute)
- [Usage and installation](#usage-and-installation)
- [Credits and references](#credits-and-references)
- [License](#license)

## Information about the game

> ### Rules

> The game uses a deck of 36, 52 or 54 cards. The game can be played from two to eight players.

> The deck is distributed equally to all players. Players do not look at their cards, but put them in a pile next to them. The first player to take the card removes the top card from his pile and places it face up in the center of the table. The other players around the circle do the same. That player, whose card turned out to be older than all the others, removes his own and "broken" cards and puts them in another pile (option: at the bottom of his pile); the order of folding cards in different versions of the game can be subject to certain rules or be arbitrary, which allows one or another strategy to be pursued in order to capture the highest possible cards from the opponent.

> The player who has lost all his cards is out of the game.

> The winner is the player who has the entire deck in the pile. A giveaway game is also possible, in which the winner is the one who gets rid of his cards before the rest.

> ### Dispute

> If two or more players have the same cards (this situation is called a "dispute"), then each of these players puts one more card on top, and the one whose card turned out to be older than all the others removes the cards. Option - each "disputing" player lays out two cards, one face-down ("mortgage"), and one open, according to which it is determined who takes the cards lying on the line. If among three players two arguing cards are less than the third, then the third one with the higher card automatically wins, and the dispute is canceled. If a player has no cards to hold a dispute, then he takes all the cards of the dispute. If the player has one card left, then the dispute goes on without a gap.

## Usage and installation

1. Upgrade required packages with `pip install -r requirements.txt --upgrade` (if you don't have one, it will be automatically installed).
2. Edit global variables in [`main.py`](src/main.py) if you want.
3. Run the `main.py` with `python src/main.py`.

## Credits and references

[Wikipedia page](https://en.wikipedia.org/wiki/War_(card_game)) about the English version of the game.
[Wikipedia page](https://ru.wikipedia.org/wiki/%D0%9F%D1%8C%D1%8F%D0%BD%D0%B8%D1%86%D0%B0_(%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F_%D0%B8%D0%B3%D1%80%D0%B0)) about the Russian version of the game.

## License

[Pyanitsa Simulation](https://github.com/8nhuman8/pyanitsa-simulation) specific code is distributed under [MIT License](https://github.com/8nhuman8/pyanitsa-simulation/blob/master/LICENSE).

Copyright (c) 2022 Artyom Bezmenov
