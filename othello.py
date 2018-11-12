import time
import player
import game
import os

tabuleiro = game.Tabuleiro()

print("#########################################")
print("0 - Facil")
print("1 - Medio")
print("2 - Dificil")
print("#########################################")
difficult = int(input("Digite o numero da dificuldade desejado: "))

if difficult == 0:
    while difficult == 0:
        os.system('clear')
        print("\n\nFRACO!\nEscolha um nível mais dificil")
        print()
        print("0 - Facil")
        print("1 - Medio")
        print("2 - Dificil")
        difficult = int(input("Digite o numero da dificuldade desejado: "))
    
os.system('clear')
        
#white_pieces = white.get_pieces(tabuleiro.get_tabuleiro())  # list of pieces

#white.get_valid_plays(white_pieces, tabuleiro.get_tabuleiro())
#white.run_play(tabuleiro.get_tabuleiro())

tabuleiro._print_tabuleiro()

white = player.Player("White")
black = player.Player("Black")
ai = player.AI("Black", difficult)

game.Game(tabuleiro, white, ai)