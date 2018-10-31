from abc import ABC, abstractmethod
from colorama import init 
from termcolor import colored
import time

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

    @abstractmethod
    def has_valid_plays(self, **kargs):
        raise NotImplementedError


class Player(Abstract_Player):
    def __init__(self, player_color):
        super().__init__(player_color)

    def run_play(self, tabuleiro):
        self.get_valid_plays(self.get_pieces(tabuleiro), tabuleiro)
        print("----------------")
        print("Suas opcoes sao:")
        cont = 0
        for p in self.possible_plays:
            print(cont, ":", p)
            cont += 1       
        print("\nDeseja escolher qual opcao?")
        
        print("----------------")
        text = input("Digite o indice: ")
        print(text)
        print(self.possible_plays[int(text)])

        play = self.possible_plays[int(text)]
        row = play[0]
        col = play[1]
        play_value = play[2]
        self.play_catch(row, col, tabuleiro)
        tabuleiro[row][col] = self.player

    def play_catch(self, row, col, tabuleiro):
        has_left_play = False
        left_catch = 0
        col_aux = col
        while(
            col_aux-1 >= 0 and
            tabuleiro[row][col_aux-1] != self.player and
            tabuleiro[row][col_aux-1] is not None    
        ):
            has_left_play = True
            col_aux -= 1
            left_catch += 1    
        if has_left_play and col_aux-1 >= 0 and tabuleiro[row][col_aux-1] == self.player: 
            #self.possible_plays.append((row, col-1, left_catch))
            for i in range(col_aux-1, col):
                tabuleiro[row][i] = self.player
                #print(i)

        has_right_play = False
        right_catch = 0
        col_aux = col
        print("Actual row: {} col: {} ".format(row, col))
        while(
            col_aux+1 < 8 and
            tabuleiro[row][col_aux+1] != self.player and
            tabuleiro[row][col_aux+1] is not None
        ):
            print("ENtrei DENTRO PORRAIFAOISHFOSIJHFOJW")
            has_right_play = True
            col_aux += 1
            right_catch += 1    
        if has_right_play and col_aux+1 < 8 and tabuleiro[row][col_aux+1] == self.player: 
            # self.possible_plays.append((row, col-1, left_catch))
            print("Col: ")
            for i in range(col, col_aux+1):
                print(i)
                tabuleiro[row][i] = self.player
                # print(i)

        has_up_play = False
        up_catch = 0
        row_aux = row
        while(
            row_aux-1 >= 0 and 
            tabuleiro[row_aux-1][col] != self.player and
            tabuleiro[row_aux-1][col] is not None
            
        ):
            has_up_play = True
            row_aux -= 1
            up_catch += 1    
        if has_up_play and row_aux-1 >= 0 and tabuleiro[row_aux-1][col] == self.player: 
            # self.possible_plays.append((row, col-1, left_catch))
            for i in range(row_aux-1, row):
                tabuleiro[i][col] = self.player
                # print(i)
        
        has_down_play = False
        down_catch = 0
        row_aux = row
        print("ROW AUX: ", row_aux)
        while(
            row_aux+1 < 8 and
            tabuleiro[row_aux+1][col] != self.player and
            tabuleiro[row_aux+1][col] is not None
        ):
            has_down_play = True
            row_aux += 1
            down_catch += 1    
        if has_down_play and row_aux+1 < 8 and tabuleiro[row_aux+1][col] == self.player: 
            # self.possible_plays.append((row, col-1, left_catch))
            for i in range(row, row_aux+1):
                tabuleiro[i][col] = self.player
                # print(i)

    def get_valid_plays(self, my_pieces, tabuleiro):
        self.possible_plays = []
        for piece in my_pieces:
            #print(piece)
            #self.diagonal_catch(piece, tabuleiro)
            self.side_catch(piece, tabuleiro)
        return None if len(self.possible_plays) == 0 else self.possible_plays
        
    def has_valid_plays(self, tabuleiro):
        if self.get_valid_plays(self.get_pieces(tabuleiro), tabuleiro) is None:
            return False
        else:
            return True

    def side_catch(self, piece, tabuleiro):
        row = piece[0]
        col = piece[1]

        has_left_play = False
        left_catch = 0
        while(
            col-1 >= 0 and
            tabuleiro[row][col-1] != self.player and
            tabuleiro[row][col-1] is not None    
            
        ):
            has_left_play = True
            col -= 1
            left_catch += 1    
        if has_left_play and col-1 >= 0 and tabuleiro[row][col-1] is None: 
            self.possible_plays.append((row, col-1, left_catch))

        row = piece[0]
        col = piece[1]
        has_right_play = False
        right_catch = 0
        while(
            col+1 < 8 and
            tabuleiro[row][col+1] != self.player and
            tabuleiro[row][col+1] is not None   
            
        ):
            has_right_play = True
            col += 1  
            right_catch += 1
        if has_right_play and col+1 < 8 and tabuleiro[row][col+1] is None: 
            self.possible_plays.append((row, col+1, right_catch))

        row = piece[0]
        col = piece[1]
        has_up_play = False
        up_catch = 0
        while(
            row-1 >= 0 and
            tabuleiro[row-1][col] != self.player and
            tabuleiro[row-1][col] is not None    
            
        ):
            has_up_play = True
            row -= 1
            up_catch += 1
        if has_up_play and row-1 >= 0 and tabuleiro[row-1][col] is None: 
            self.possible_plays.append((row-1, col, up_catch))

        row = piece[0]
        col = piece[1]
        has_down_play = False 
        down_catch = 0
        while(
            row+1 < 8 and
            tabuleiro[row+1][col] != self.player and
            tabuleiro[row+1][col] is not None
        ):
            has_down_play = True
            row += 1
            down_catch += 1
        if has_down_play and row+1 < 8 and tabuleiro[row+1][col] is None: 
            self.possible_plays.append((row+1, col, down_catch))
        
        #print(self.possible_plays)
        #self.plays = possible_plays

    def diagonal_catch(self, piece, tabuleiro):
        #print(tabuleiro[piece[0]][piece[1]])
        row = piece[0]
        col = piece[1]
        while(
            tabuleiro[row-1][col-1] != self.player and
            tabuleiro[row-1][col-1] is not None and    
            row-1 > 0 and
            col-1 > 0
        ):
            print("Diagonal")
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


class AI(Abstract_Player):
    def __init__(self, player_color):
        super().__init__(player_color)

    def get_pieces(self):
        pass
    
    def get_player_score(self):
        pass
    
    def get_valid_plays(self):
        pass
    
    def has_valid_plays(self):
        pass