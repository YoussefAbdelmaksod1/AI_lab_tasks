## Main Functionality of the program :

1. **Import necessary libraries**: The code starts by importing necessary libraries, including Pygame for creating the GUI, numpy for representing the game board as a numpy array, and random for generating random moves for the AI.

2. **Define game constants**: Some constants are defined, such as the width and height of the game board, the size of each square, the line width, the radius of the circles, and the offset for drawing the cross and circle symbols.

3. **Define colors**: The colors used in the game are defined, including the background color, line color, cross color, and circle color.

4. **Initialize Pygame**: The Pygame library is initialized, and the game screen is set up with a specified width and height. The screen is filled with the background color.

5. **Define the Board class**: The Board class represents the game board. It has a 2D numpy array called squares to represent the state of the board, with 0 indicating an empty square, 1 indicating a cross, and 2 indicating a circle. It also has a copy of the empty squares for AI calculations and a count of the number of marked squares. The Board class has a final_state method that checks if there is a winner or a draw and returns 1 for a cross win, 2 for a circle win, 0 for no winner yet, and -1 for a draw.

6. **Define the AI class**: The AI class represents the AI player. It has a level attribute that can be 0 or 1, with 0 indicating a random AI and 1 indicating a minimax AI. The AI class has an eval method that evaluates the board state and returns a move (row, col) for the AI to make. The eval method uses the minimax algorithm for level 1 AI and a random choice for level 0 AI.

7. **Define the Game class**: The Game class represents the overall game. It has a Board object, an AI object, the current player (1 for cross, 2 for circle), the game mode (either 'pvp' or 'ai'), a running flag to indicate whether the game is still running, and methods for drawing the game board and making moves. The Game class also has an isover method that checks if the game is over and returns True if there is a winner or a draw.

8. **Draw methods**: The show_lines method draws the lines of the game board, and the draw_symbol method draws a cross or a circle in a specified square.

9. **Gameplay methods**: The make_move method updates the board state and draws the symbol for the current player. The isover method checks if the game is over and returns True if there is a winner or a draw.

10. **AI methods**: The ai_move method is called when it is the AI's turn to move. It updates the screen, gets the AI's move, makes the move, and checks if the game is over.

11. **Main function**: The main function creates a Game object and enters the game loop. In the game loop, events are handled, and the game is updated accordingly. If the game is over, the running flag is set to False, and the game loop exits.
