from game import Game


game = Game(2)
for player in game.players:
    print(player.hand, end='\n\n')
