import tkinter as tk
from tkinter import messagebox

class BattleshipGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Battleship Game")
        self.board_size = 8
        self.board_player1 = [['O' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board_player2 = [['O' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ship_sizes = [2, 3, 3, 4, 5]
        self.ships_player1 = []
        self.ships_player2 = []
        self.hits_player1 = 0
        self.hits_player2 = 0
        self.current_player = 1  # Player 1 starts first
        self.create_widgets()
        self.place_ships()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Battleship Game", font=("Arial", 18))
        self.label.pack(pady=10)

        self.player_label = tk.Label(self.master, text=f"Player {self.current_player}'s Turn", font=("Arial", 12))
        self.player_label.pack()

        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        self.buttons = []
        for row in range(self.board_size):
            row_buttons = []
            for col in range(self.board_size):
                button = tk.Button(self.board_frame, text="O", width=2, command=lambda r=row, c=col: self.guess_location(r, c))
                button.grid(row=row, column=col, padx=1, pady=1)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.message_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.message_label.pack(pady=10)

        self.battle_counts_label = tk.Label(self.master, text="Battle Counts", font=("Arial", 14, "bold"))
        self.battle_counts_label.pack()

        self.counts_frame = tk.Frame(self.master)
        self.counts_frame.pack()

        self.player1_label = tk.Label(self.counts_frame, text=f"Player 1: {self.hits_player1}", font=("Arial", 12))
        self.player1_label.pack(side=tk.LEFT, padx=20)

        self.player2_label = tk.Label(self.counts_frame, text=f"Player 2: {self.hits_player2}", font=("Arial", 12))
        self.player2_label.pack(side=tk.RIGHT, padx=20)

    def place_ships(self):
        # Example ship placements
        self.place_ship(1, 2, (0, 0), (0, 1))  # Player 1 ship placement
        self.place_ship(1, 3, (2, 3), (4, 3))  # Player 1 ship placement
        self.place_ship(2, 3, (7, 7), (7, 5))  # Player 2 ship placement
        self.place_ship(2, 4, (3, 2), (6, 2))  # Player 2 ship placement

    def place_ship(self, player, ship_size, start, end):
        board = self.board_player1 if player == 1 else self.board_player2
        if start[0] == end[0] and abs(start[1] - end[1]) == ship_size - 1:
            for col in range(start[1], end[1] + 1):
                board[start[0]][col] = 'S'
        elif start[1] == end[1] and abs(start[0] - end[0]) == ship_size - 1:
            for row in range(start[0], end[0] + 1):
                board[row][start[1]] = 'S'
        else:
            print("Invalid ship placement. Please try again.")

    def guess_location(self, row, col):
        if self.current_player == 1:
            if self.board_player2[row][col] == 'S':
                self.board_player2[row][col] = 'X'
                self.hits_player1 += 1
                self.buttons[row][col].config(text="X", state=tk.DISABLED)
                self.message_label.config(text="Player 1: Hit!")
            else:
                self.board_player2[row][col] = '-'
                self.buttons[row][col].config(text="-", state=tk.DISABLED)
                self.message_label.config(text="Player 1: Miss!")
            self.update_battle_counts()
            self.check_winner()
            self.current_player = 2
            self.player_label.config(text="Player 2's Turn")
        else:
            if self.board_player1[row][col] == 'S':
                self.board_player1[row][col] = 'X'
                self.hits_player2 += 1
                self.buttons[row][col].config(text="X", state=tk.DISABLED)
                self.message_label.config(text="Player 2: Hit!")
            else:
                self.board_player1[row][col] = '-'
                self.buttons[row][col].config(text="-", state=tk.DISABLED)
                self.message_label.config(text="Player 2: Miss!")
            self.update_battle_counts()
            self.check_winner()
            self.current_player = 1
            self.player_label.config(text="Player 1's Turn")

    def update_battle_counts(self):
        self.player1_label.config(text=f"Player 1: {self.hits_player1}")
        self.player2_label.config(text=f"Player 2: {self.hits_player2}")

    def check_winner(self):
        if self.hits_player1 == sum(self.ship_sizes):
            messagebox.showinfo("Game Over", "Player 1 wins!")
            self.reset_game()
        elif self.hits_player2 == sum(self.ship_sizes):
            messagebox.showinfo("Game Over", "Player 2 wins!")
            self.reset_game()

    def reset_game(self):
        self.board_player1 = [['O' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board_player2 = [['O' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.hits_player1 = 0
        self.hits_player2 = 0
        self.current_player = 1
        self.player_label.config(text="Player 1's Turn")
        self.message_label.config(text="")
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].config(text="O", state=tk.NORMAL)
        self.update_battle_counts()

root = tk.Tk()
game = BattleshipGUI(root)
root.mainloop()
