from colorama import init 
from termcolor import colored
from abc import ABC, abstractmethod


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
        self._print_tabuleiro()

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


class Abstract_Player(ABC):
    def __init__(self, player_color):
        self.player = player_color
        self.player_score = 0
        super().__init__()

    @abstractmethod
    def get_valid_plays(self, **kargs):
        raise NotImplementedError
    
    @abstractmethod
    def get_player_score(self, **kargs):
        raise NotImplementedError

    @abstractmethod
    def get_pieces(self, **kargs):
        raise NotImplementedError


class Player(Abstract_Player):
    def __init__(self, player_color):
        super().__init__(player_color)

    def get_valid_plays(self, my_pieces, tabuleiro):
        for piece in my_pieces:
            print(piece)
            self.diagonal_catch(piece, tabuleiro)
            self.side_catch(piece, tabuleiro)
        pass

    def side_catch(self, piece, tabuleiro):
        possible_plays = []
        row = piece[0]
        col = piece[1]

        has_left_play = False
        while(
            tabuleiro[row][col-1] != self.player and
            tabuleiro[row][col-1] is not None and    
            col-1 >= 0
        ):
            has_left_play = True
            col -= 1    
        if has_left_play and col-1 >= 0: 
            possible_plays.append((row, col-1))

        row = piece[0]
        col = piece[1]
        has_right_play = False
        while(
            tabuleiro[row][col+1] != self.player and
            tabuleiro[row][col+1] is not None and    
            col+1 < 8
        ):
            has_right_play = True
            col += 1  
        if has_right_play and col+1 < 8: 
            possible_plays.append((row, col+1))

        row = piece[0]
        col = piece[1]
        has_up_play = False
        while(
            tabuleiro[row-1][col] != self.player and
            tabuleiro[row-1][col] is not None and    
            row-1 >= 0
        ):
            has_up_play = True
            row -= 1
        if has_up_play and row-1 >= 0: 
            possible_plays.append((row-1, col))

        row = piece[0]
        col = piece[1]
        has_down_play = False 
        while(
            tabuleiro[row+1][col] != self.player and
            tabuleiro[row+1][col] is not None and    
            row+1 < 8
        ):
            has_down_play = True
            row += 1
        if has_down_play and row+1 < 8: 
            possible_plays.append((row+1, col))
        
        print(possible_plays)

    def diagonal_catch(self, piece, tabuleiro):
        print(tabuleiro[piece[0]][piece[1]])
        row = piece[0]
        col = piece[1]
        while(
            tabuleiro[row-1][col-1] != self.player and
            tabuleiro[row-1][col-1] is not None and    
            row-1 > 0 and
            col-1 > 0
        ):
            print(row-1)
            print(col-1)

            

    def get_player_score(self):
        print(self.player_score)
        pass
    
    def get_pieces(self, tabuleiro):
        pieces = []
        for row in range(0, len(tabuleiro)):
            for col in range(0, len(tabuleiro[0])):
                if tabuleiro[row][col] == self.player:
                    pieces.append((row, col))
        return pieces    
    
tabuleiro = Tabuleiro()

white = Player("White")
white_pieces = white.get_pieces(tabuleiro.get_tabuleiro())  # list of pieces

white.get_valid_plays(white_pieces, tabuleiro.get_tabuleiro())

