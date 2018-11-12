from abc import ABC, abstractmethod
from colorama import init 
from termcolor import colored
import time
import sys
import copy

DEPTH_NUM = 3

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
        self.execute_catch(row, col, tabuleiro)
        tabuleiro[row][col] = self.player

    def execute_catch(self, row, col, tabuleiro, player=None):
        """
            Lateral catchs
        """
        if player is None:
            player = self.player

        has_left_play = False
        left_catch = 0
        col_aux = col
        while(
            col_aux-1 >= 0 and
            tabuleiro[row][col_aux-1] != player and
            tabuleiro[row][col_aux-1] is not None    
        ):
            has_left_play = True
            col_aux -= 1
            left_catch += 1    
        if has_left_play and col_aux-1 >= 0 and tabuleiro[row][col_aux-1] == player: 
            #self.possible_plays.append((row, col-1, left_catch))
            for i in range(col_aux-1, col):
                tabuleiro[row][i] = player
                #print(i)

        has_right_play = False
        right_catch = 0
        col_aux = col
        #print("Actual row: {} col: {} ".format(row, col))
        while(
            col_aux+1 < 8 and
            tabuleiro[row][col_aux+1] != player and
            tabuleiro[row][col_aux+1] is not None
        ):
        #    print("ENtrei DENTRO PORRAIFAOISHFOSIJHFOJW")
            has_right_play = True
            col_aux += 1
            right_catch += 1    
        if has_right_play and col_aux+1 < 8 and tabuleiro[row][col_aux+1] == player: 
            # self.possible_plays.append((row, col-1, left_catch))
        #    print("Col: ")
            for i in range(col, col_aux+1):
                #print(i)
                tabuleiro[row][i] = player
                # print(i)

        has_up_play = False
        up_catch = 0
        row_aux = row
        while(
            row_aux-1 >= 0 and 
            tabuleiro[row_aux-1][col] != player and
            tabuleiro[row_aux-1][col] is not None
            
        ):
            has_up_play = True
            row_aux -= 1
            up_catch += 1    
        if has_up_play and row_aux-1 >= 0 and tabuleiro[row_aux-1][col] == player: 
            # self.possible_plays.append((row, col-1, left_catch))
            for i in range(row_aux-1, row):
                tabuleiro[i][col] = player
                # print(i)
        
        has_down_play = False
        down_catch = 0
        row_aux = row
        while(
            row_aux+1 < 8 and
            tabuleiro[row_aux+1][col] != player and
            tabuleiro[row_aux+1][col] is not None
        ):
            has_down_play = True
            row_aux += 1
            down_catch += 1    
        if has_down_play and row_aux+1 < 8 and tabuleiro[row_aux+1][col] == player: 
            # self.possible_plays.append((row, col-1, left_catch))
            for i in range(row, row_aux+1):
                tabuleiro[i][col] = player
                # print(i)

        """
            Diagonaol Catchs
        """
        has_upper_left_play = False
        upper_left_catch = 0
        row_aux = row
        col_aux = col
        while(
            row_aux-1 >= 0 and
            col_aux-1 >= 0 and
            tabuleiro[row_aux-1][col_aux-1] != player and
            tabuleiro[row_aux-1][col_aux-1] is not None
        ):
            has_upper_left_play = True
            row_aux -= 1
            col_aux -= 1
            upper_left_catch += 1    
        if has_upper_left_play and row_aux-1 >= 0 and col_aux-1 >= 0 and tabuleiro[row_aux-1][col_aux-1] == player: 
            for i in range(upper_left_catch+1):
                tabuleiro[row-i][col-i] = player


        #####
        #####   Upper right
        #####   
        has_upper_right_play = False
        upper_right_catch = 0
        row_aux = row
        col_aux = col
        while(
            row_aux-1 >= 0 and
            col_aux+1 < 8 and
            tabuleiro[row_aux-1][col_aux+1] != player and
            tabuleiro[row_aux-1][col_aux+1] is not None
        ):
            has_upper_right_play = True
            row_aux -= 1
            col_aux += 1
            upper_right_catch += 1    
        if has_upper_right_play and row_aux-1 >= 0 and col_aux+1 < 8 and tabuleiro[row_aux-1][col_aux+1] == player: 
            for i in range(upper_right_catch+1):
                tabuleiro[row-i][col+i] = player


        #####
        #####   Lower right
        #####
        has_lower_right_play = False
        lower_right_catch = 0
        row_aux = row
        col_aux = col
        while(
            row_aux+1 < 8 and
            col_aux+1 < 8 and
            tabuleiro[row_aux+1][col_aux+1] != player and
            tabuleiro[row_aux+1][col_aux+1] is not None
        ):
            has_lower_right_play = True
            row_aux += 1
            col_aux += 1
            lower_right_catch += 1    
        if has_lower_right_play and row_aux+1 < 8 and col_aux+1 < 8 and tabuleiro[row_aux+1][col_aux+1] == player: 
            for i in range(lower_right_catch+1):
                tabuleiro[row+i][col+i] = player


        #####
        #####   Lower left
        #####
        has_lower_left_play = False
        lower_left_catch = 0
        row_aux = row
        col_aux = col
        while(
            row_aux+1 < 8 and
            col_aux-1 >= 0 and
            tabuleiro[row_aux+1][col_aux-1] != player and
            tabuleiro[row_aux+1][col_aux-1] is not None
        ):
            has_lower_left_play = True
            row_aux += 1
            col_aux -= 1
            lower_left_catch += 1    
        if has_lower_left_play and row_aux+1 < 8 and col_aux-1 >= 0 and tabuleiro[row_aux+1][col_aux-1] == player: 
            for i in range(lower_left_catch+1):
                tabuleiro[row+i][col-i] = player



    def get_valid_plays(self, tabuleiro):
        my_pieces = self.get_pieces(tabuleiro)
        self.possible_plays = []
        for piece in my_pieces:
            #print(piece)
            self.side_catch(piece, tabuleiro)
            self.diagonal_catch(piece, tabuleiro)
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
            #self.possible_plays.append((row, col-1, left_catch))
            if (row, col-1, left_catch) not in self.possible_plays:
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
            #self.possible_plays.append((row, col+1, right_catch))
            if (row, col+1, right_catch) not in self.possible_plays:
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
            #self.possible_plays.append((row-1, col, up_catch))
            if (row+1, col, up_catch) not in self.possible_plays:
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
            #self.possible_plays.append((row+1, col, down_catch))
            if (row+1, col, down_catch) not in self.possible_plays:
                    self.possible_plays.append((row+1, col, down_catch))
        #print(self.possible_plays)
        #self.plays = possible_plays

    def diagonal_catch(self, piece, tabuleiro, player=None):
        if player is None:
            player = self.player
        #print(tabuleiro[piece[0]][piece[1]])

        """
            Upper left
        """
        row = piece[0]
        col = piece[1]
        upper_left_catch = 0
        has_upper_left_play = False
        while(
            tabuleiro[row-1][col-1] != player and
            tabuleiro[row-1][col-1] is not None and    
            row-1 > 0 and
            col-1 > 0
        ):
            #print("Diagonal")
            has_upper_left_play = True
            col -= 1
            row -= 1
            upper_left_catch += 1    
        if has_upper_left_play and col-1 >= 0 and row-1 >= 0 and tabuleiro[row-1][col-1] is None: 
            if (row-1, col-1, upper_left_catch) not in self.possible_plays:
                self.possible_plays.append((row-1, col-1, upper_left_catch))
            #self.possible_plays.append((row, col-1, left_catch))

        """
            Upper right
        """
        row = piece[0]
        col = piece[1]
        upper_right_catch = 0
        has_upper_right_play = False
        while(
            row-1 >= 0 and
            col+1 < 8 and
            tabuleiro[row-1][col+1] != player and
            tabuleiro[row-1][col+1] is not None    
        ):
            has_upper_right_play = True
            col += 1
            row -= 1
            upper_right_catch += 1    
        if has_upper_right_play and col+1 < 8 and row-1 >= 0 and tabuleiro[row-1][col+1] is None: 
            if (row-1, col+1, upper_right_catch) not in self.possible_plays:
                self.possible_plays.append((row-1, col+1, upper_right_catch))
            #self.possible_plays.append((row, col-1, left_catch))
        

        """
            Lower Right
        """
        row = piece[0]
        col = piece[1]
        lower_right_catch = 0
        has_lower_right_play = False
        while(
            row+1 < 8 and
            col+1 < 8 and
            tabuleiro[row+1][col+1] != player and
            tabuleiro[row+1][col+1] is not None    
        ):
            has_lower_right_play = True
            col += 1
            row += 1
            lower_right_catch += 1    
        if has_lower_right_play and col+1 < 8 and row+1 < 8 and tabuleiro[row+1][col+1] is None: 
            if (row+1, col+1, lower_right_catch) not in self.possible_plays:
                self.possible_plays.append((row+1, col+1, lower_right_catch))
            #self.possible_plays.append((row, col-1, left_catch))


        """ 
            Lower Left
        """
        row = piece[0]
        col = piece[1]
        lower_left_catch = 0
        has_lower_left_play = False
        while(
            row+1 < 8 and
            col-1 > 0 and
            tabuleiro[row+1][col-1] != player and
            tabuleiro[row+1][col-1] is not None    
        ):
            has_lower_left_play = True
            col -= 1
            row += 1
            lower_left_catch += 1    
        if has_lower_left_play and col-1 >= 0 and row+1 < 8 and tabuleiro[row+1][col-1] is None: 
            if (row+1, col-1, lower_left_catch) not in self.possible_plays:
                self.possible_plays.append((row+1, col-1, lower_left_catch))
            #self.possible_plays.append((row, col-1, left_catch))



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
    def __init__(self, player_color, difficult_level):
        super().__init__(player_color)
        if difficult_level == 1:
            self.difficult_level = 1
        elif difficult_level == 2:
            self.difficult_level = 3
        elif difficult_level == 3:
            self.difficult_level = 5
        
    def get_enemy_pieces(self, tabuleiro):
        pieces = []
        #print("Player: ", self.player)
        for row in range(0, len(tabuleiro)):
            for col in range(0, len(tabuleiro[0])):
                #print("Player=", self.player)
                if tabuleiro[row][col] != self.player and tabuleiro[row][col] is not None:
                #    print("Position: ", tabuleiro[row][col])
                    pieces.append((row, col))
        return pieces   

    def get_valid_enemy_plays(self, board):
        enemy_pieces = self.get_enemy_pieces(board)
        #print("Enemy pieces: ", enemy_pieces)
        self.possible_plays = []
        for piece in enemy_pieces:
            #print(piece)
            #self.diagonal_catch(piece, tabuleiro)
            self.side_catch(piece, board, player='White')  # IF PLAYER1 is WHITE
            self.diagonal_catch(piece, board, player='White')
        return None if len(self.possible_plays) == 0 else self.possible_plays

    def run_play(self, tabuleiro, ai_depth=3):
        """
            Here MINIMAX starts. First we get the valid plays. For each valid play, 
        """
        self.tabuleiro = copy.deepcopy(tabuleiro)
        plays = self.get_valid_plays(tabuleiro)
        print("START MINIMAX")
                
        eval, play_coord = self.minimax(self.tabuleiro, None, self.difficult_level, True)
        print("END OF MINIMAX: {}<-->{}".format(eval, play_coord))
        #print(plays)
        self.execute_catch(play_coord[0], play_coord[1], tabuleiro, player="Black")
        tabuleiro[play_coord[0]][play_coord[1]] = self.player
        
        print(ai_depth)
        


    def minimax(self, ai_board, player_play, depth, maximizing):
        if depth == 0:
            return self._eval_board(ai_board), player_play
        
        if maximizing:
            maxEval = -sys.maxsize
            maxPlay = None
            ai_plays = self.get_valid_plays(ai_board)

            # Return board evaluation if no more plays avaiable
            if ai_plays is None:
                return self._eval_board(ai_board), player_play
            for play in ai_plays:
                actual_board = copy.deepcopy(ai_board)
                self.execute_catch(play[0], play[1], actual_board, player="Black")
                actual_board[play[0]][play[1]] = self.player
                if depth == self.difficult_level:
                    eval, play_coord = self.minimax(actual_board, play, depth - 1, False)
                else:
                    eval, play_coord = self.minimax(actual_board, player_play, depth - 1, False)
                if maxEval < eval:
                    maxEval = eval
                    maxPlay = play_coord
            return maxEval, maxPlay
        else:
            minEval = sys.maxsize
            minPlay = None
            enemy_plays = self.get_valid_enemy_plays(ai_board)

            # Return board evaluation if no more plays avaiable
            if enemy_plays is None:
                return self._eval_board(ai_board), player_play
            for enemy_play in enemy_plays:
                actual_board = copy.deepcopy(ai_board)
                self.execute_catch(enemy_play[0], enemy_play[1], actual_board, player="White")
                actual_board[enemy_play[0]][enemy_play[1]] = "White"
                eval, play_coord  = self.minimax(actual_board, player_play, depth - 1, True)
                if minEval > eval:
                    minEval = eval
                    minPlay = play_coord
            return minEval, minPlay

    def _eval_board(self, tabuleiro):
        white = 0
        black = 0
        for row in tabuleiro:
            #print(row)
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
                    print("Espace", end="\t")
            print("\n")  
        print("---------------------------------------------------------------------")