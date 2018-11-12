from colorama import init 
from termcolor import colored

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        for i in range(0, 8):
            row = []
            for j in range(0, 8):
                row.append(None)
            self.tabuleiro.append(row)            
        self._generate_black()
        self._generate_white()
        #self._print_tabuleiro()

    def get_tabuleiro(self):
        return self.tabuleiro

    def _generate_white(self):
        self.tabuleiro[3][3] = 'White'
        self.tabuleiro[4][4] = 'White'

    def _generate_black(self):
        self.tabuleiro[3][4] = 'Black'
        self.tabuleiro[4][3] = 'Black'

    def _print_tabuleiro(self):
        print("---------------------------------------------------------------------")
        print(end="\t")
        for i in range(0, 8):
            print(i, end="\t")
        print("\n")

        cont = 0
        for row in self.tabuleiro:
            print(cont, end="\t")
            cont += 1
            for cell in row:
                if cell == "White":
                    print(colored('WHITE', 'blue'), end="\t")
                elif cell == "Black":
                    print(colored('BLACK', 'red'), end="\t")
                else:
                    print(cell, end="\t")
            print("\n")  
        print("---------------------------------------------------------------------")

    def eval_board(self):
        white = 0
        black = 0
        for row in self.tabuleiro:
            #print(row)
            for cell in row:
                if cell == 'White':
                    white += 1
                elif cell == 'Black':
                    black += 1
        return (black-white)

class Game:
    def __init__(self, tabuleiro, player1, player2, difficult_level=1):
        self.tabuleiro = tabuleiro
        self.player1 = player1
        self.player2 = player2
        self.difficult_level = difficult_level
        self.game_loop()
    
    def get_next_player(self):
        return self.player1 if self.actual_player is self.player2 else self.player2

    def game_loop(self):
        self.actual_player = self.player1 
        while(
            self.actual_player.has_valid_plays(self.tabuleiro.get_tabuleiro())
        ):
            print("---------------\nACTUAL PLATER: {} \n---------------".format(self.actual_player.player))
            self.actual_player.run_play(self.tabuleiro.get_tabuleiro())
            
            self.tabuleiro._print_tabuleiro()
            
            self.actual_player = self.get_next_player()
            
             #valid_plays = self.actual_player.get_valid_plays(self.actual_player.get_pieces, self.tabuleiro.get_tabuleiro())
        
              
            #time.sleep(1)
        pass