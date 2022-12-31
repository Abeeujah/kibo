# Final Project For Try With Kibo..
# A GUI Tic Tac Toe Game

# Import tkinter to create the GUI platform..
import tkinter as tk
from tkinter import font

# Import NamedTuple From Type Module..
from typing import NamedTuple

# Import Cycle From Itertools
from itertools import cycle

# Define Player Class..

class Player(NamedTuple):
    label: str
    color: str

# Define Move(s) Class..

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

# Player * Board..
BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green")
)

# Game Logic Controller..

class TicGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    # Set Up The Board..
    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    # Possible Win Combo..
    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    # Validate Moves..
    def valid_move(self, move):
        '''Validate Move and Return True or False'''
        row, col = move.row, move.col
        not_moved = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and not_moved

    # Move Processes..
    def process_move(self, move):
        '''Process Current move and Decide if It\'s a Win.'''
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            # Using Set to Collate all Moves Into One
            results = set(
                self._current_moves[n][m].label
                for n, m in combo
            )
            # Winner If The Combo is matched and all entry is flattened to one
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    # Function to Check if the Game Has a Winner..
    def has_winner(self):
        '''Return True or False if the game has a winner'''
        return self._has_winner

    # Check if the game is tied..
    def is_tied(self):
        '''Return True if the Game is tied or false Otherwise'''
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row)
        return no_winner and all(played_moves)

    # Toggle Players after Valid Moves..
    def toggle_player(self):
        '''Toggles And Returns the Toggled Player'''
        self.current_player = next(self._players)

    # Reset Game..
    def reset_game(self):
        '''Reset Game State To Play Again'''
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
            self._has_winner = False
            self.winner_combo = []

# Create Game Board and make it Inherit from tkinter class..

class TicBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title('Tic Tac Toe Game')
        self._cells = {}
        self._game = game
        self._create_menu()
        self.board_display()
        self.board_grid()

    # Add Menu Contols to the GUI..
    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    # Board Display..
    def board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame, text="Ready?", font=font.Font(size=28, weight='bold'),)
        self.display.pack()

    # Board Grid
    def board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame, text='', font=font.Font(
                        size=36, weight='bold'), fg='black', width=3, height=2, highlightbackground='lightblue',
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    # Handle Players Moves Using Tkinter's Events
    def play(self, event):
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            elif self._game.has_winner():
                self._update_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    # Update GUI Buttons..
    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    # Update GUI Display..
    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    # Update GUI to Highlight Win Cells..
    def _update_cells(self):
        for button , coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    # Reset GUI Board..
    def reset_board(self):
        '''Reset The Game\'s Board'''
        self._game.reset_game()
        self._update_display(msg="Ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")

# Run The Script and Initialize the Game..
def main():
    # Instantiate Game Loop..
    '''Instantiate Board and Run Game Loop'''
    game = TicGame()
    board = TicBoard(game)
    board.mainloop()

# Conditional to execute Game..
if __name__ == '__main__':
    main()
