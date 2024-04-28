# Import necessary libraries
import copy
import sys
import pygame
import random
import numpy as np

# Define game constants
WIDTH = 400
HEIGHT = 400
ROWS = 3
COLS = 3
SQSIZE = WIDTH // COLS
LINE_WIDTH = 15
RADIUS = SQSIZE // 4 - LINE_WIDTH // 2
OFFSET = SQSIZE // 4

# Define colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CROSS_COLOR = (66, 66, 66)
CIRC_COLOR = (239, 239, 239)

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOR)

# Define the Board class
class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))  # Create a 3x3 numpy array to represent the board
        self.empty_sqrs = self.squares  # Keep a copy of the empty squares for AI calculations
        self.marked_sqrs = 0  # Keep track of the number of marked squares

    def final_state(self, show=False):
        '''
            @return 0 if there is no win yet
            @return 1 if player 1 wins
            @return 2 if player 2 wins
        '''

        # Check vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)  # Draw a line connecting the winning squares
                    pygame.draw.line(screen, color, (iPos[0], iPos[1] + SQSIZE // 2),
                                     (iPos[0], iPos[1] - SQSIZE // 2), LINE_WIDTH)
                return self.squares[0][col]

        # Check horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (40, row * SQSIZE + SQSIZE // 2)  # Draw a line connecting the winning squares
                    pygame.draw.line(screen, color, (iPos[0] + SQSIZE // 2, iPos[1]),
                                     (iPos[0] - SQSIZE // 2, iPos[1]), LINE_WIDTH)
                return self.squares[row][0]

        # Check diagonal wins
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[0][0] == 2 else CROSS_COLOR
                iPos = (20, 20)  # Draw a line connecting the winning squares
                pygame.draw.line(screen, color, iPos, (WIDTH - 20, HEIGHT - 20), LINE_WIDTH)
            return self.squares[0][0]
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            if show:
                color = CIRC_COLOR if self.squares[0][2] == 2 else CROSS_COLOR
                iPos = (60, 60)  # Draw a line connecting the winning squares
                pygame.draw.line(screen, color, iPos, (WIDTH - 60, HEIGHT - 60), LINE_WIDTH)
            return self.squares[0][2]

        # No winner yet
        return 0


# Define the AI class
class AI:

    def __init__(self, level=0):
        self.level = level
        self.player = 2  # AI will always be player 2 (circles)

    def eval(self, main_board):
        if self.level == 0:
            # Random choice
            eval = 'random'
            move = self.rnd(main_board)
        else:
            # Minimax algorithm choice
            eval, move = self.minimax(main_board, False)

        print(f'AI has chosen to mark the square in pos {move} with an eval of: {eval}')

        return move  # row, col

    def minimax(self, board, isMaximising):
        # Terminal state
        result = board.final_state()
        if result != 0:
            if result == 1:
                return -1, None  # Loss for AI
            elif result == 2:
                return 1, None  # Win for AI
            else:
                return 0, None  # Draw

        # Evaluate all possible states
        if isMaximising:
            best_eval = -1000
            best_move = None
            for row in range(ROWS):
                for col in range(COLS):
                    if board.squares[row][col] == 0:
                        # Make the move
                        board.squares[row][col] = self.player
                        board.marked_sqrs += 1

                        # Evaluate the move
                        eval, _ = self.minimax(board, False)

                        # Undo the move
                        board.squares[row][col] = 0
                        board.marked_sqrs -= 1

                        # Update best
                        if eval > best_eval:
                            best_eval = eval
                            best_move = (row, col)

            return best_eval, best_move
        else:
            best_eval = 1000
            best_move = None
            for row in range(ROWS):
                for col in range(COLS):
                    if board.squares[row][col] == 0:
                        # Make the move
                        board.squares[row][col] = 1
                        board.marked_sqrs += 1

                        # Evaluate the move
                        eval, _ = self.minimax(board, True)

                        # Undo the move
                        board.squares[row][col] = 0
                        board.marked_sqrs -= 1

                        # Update best
                        if eval < best_eval:
                            best_eval = eval
                            best_move = (row, col)

            return best_eval, best_move

    def rnd(self, board):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if board.squares[row][col] == 0:
                    empty_sqrs.append((row, col))

        return random.choice(empty_sqrs)


# Define the Game class
#class Game:
    #under devlopment

