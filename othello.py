import time
import player
import game

tabuleiro = game.Tabuleiro()

white = player.Player("White")
black = player.Player("Black")

ai = player.AI("Black")
#white_pieces = white.get_pieces(tabuleiro.get_tabuleiro())  # list of pieces

#white.get_valid_plays(white_pieces, tabuleiro.get_tabuleiro())
#white.run_play(tabuleiro.get_tabuleiro())

#tabuleiro._print_tabuleiro()

game.Game(tabuleiro, white, ai)