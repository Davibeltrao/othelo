from abc import ABC, abstractmethod
from colorama import init 
from termcolor import colored
import time
import sys
import copy

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
        self.get_valid_plays(tabuleiro)
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

    def get_valid_plays(self, tabuleiro):
        my_pieces = self.get_pieces(tabuleiro)
        self.possible_plays = []
        for piece in my_pieces:
            #print(piece)
            #self.diagonal_catch(piece, tabuleiro)
            self.side_catch(piece, tabuleiro)
        return None if len(self.possible_plays) == 0 else self.possible_plays
        
    def has_valid_plays(self, tabuleiro):
        if self.get_valid_plays(tabuleiro) is None:
            return False
        else:
            return True

    def side_catch(self, piece, tabuleiro, player=None):
        if player is None:
            player = self.player

        row = piece[0]
        col = piece[1]

        has_left_play = False
        left_catch = 0
        while(
            col-1 >= 0 and
            tabuleiro[row][col-1] != player and
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
            tabuleiro[row][col+1] != player and
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
            tabuleiro[row-1][col] != player and
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
            tabuleiro[row+1][col] != player and
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


class AI(Player):
    def __init__(self, player_color):
        super().__init__(player_color)
    
    def get_enemy_pieces(self, tabuleiro):
        pieces = []
        for row in range(0, len(tabuleiro)):
            for col in range(0, len(tabuleiro[0])):
                if tabuleiro[row][col] != self.player and tabuleiro[row][col] is not None:
                    pieces.append((row, col))
        return pieces   

    def get_valid_enemy_plays(self, board):
        enemy_pieces = self.get_enemy_pieces(board)
        self.possible_plays = []
        for piece in enemy_pieces:
            #print(piece)
            #self.diagonal_catch(piece, tabuleiro)
            self.side_catch(piece, board, player='Black')  # IF PLAYER1 is WHITE
        return None if len(self.possible_plays) == 0 else self.possible_plays

    def run_play(self, tabuleiro, ai_depth=3):
        """
            Here MINIMAX starts. First we get the valid plays. For each valid play, 
        """
        self.tabuleiro = copy.deepcopy(tabuleiro)
        plays = self.get_valid_plays(tabuleiro)
        
        print(self.minimax(self.tabuleiro, 3, True))
        #print(plays)
        print(ai_depth)
        


    def minimax(self, ai_board, depth, maximizing):
        if depth == 0:
            return self._eval_tabuleiro(ai_board)
        
        if maximizing:
            maxEval = -sys.maxsize
            ai_plays = self.get_valid_plays(ai_board)
            for play in ai_plays:
                print("START MINIMAX")
                actual_board = copy.deepcopy(ai_board)
                self._print_tabuleiro(actual_board)
                self.play_catch(play[0], play[1], actual_board)
                actual_board[play[0]][play[1]] = self.player
                self._print_tabuleiro(actual_board)
                #print(actual_board)
                #self._print_tabuleiro(actual_board)
                eval = self.minimax(actual_board, depth - 1, False)
                maxEval = max(maxEval, eval)
            return maxEval 
        else:
            print("ENTREI AQUI APOS")
            self._print_tabuleiro(ai_board)
            minEval = sys.maxsize
            enemy_plays = self.get_valid_enemy_plays(ai_board)
            for enemy_play in enemy_plays:
                actual_board = copy.deepcopy(ai_board)
                self.play_catch(enemy_play[0], enemy_play[1], actual_board)
                actual_board[enemy_play[0]][enemy_play[1]] = "White"
                eval = self.minimax(actual_board, depth - 1, True)
                minEval = min(minEval, eval)
            return minEval

    def _eval_tabuleiro(self, tabuleiro):
        white = 0
        black = 0
        for row in tabuleiro:
            print(row)
            for cell in row:
                if cell == 'White':
                    white += 1
                elif cell == 'Black':
                    black += 1
        return (black-white)

    def _print_tabuleiro(self, board):
        print("---------------------------------------------------------------------")
        print(end="\t")
        for i in range(0, 8):
            print(i, end="\t")
        print("\n")

        cont = 0
        for row in board:
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