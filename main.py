import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
window = tk.Tk()
window.title("Ludo Game")

# Create the canvas for the game board
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Draw the Ludo game board
canvas.create_rectangle(50, 50, 450, 450, fill="white")
canvas.create_rectangle(100, 100, 400, 400, fill="light green")

# Create a list of Ludo game pieces
game_pieces = []

# Function to create a Ludo game piece
def create_game_piece(x, y, color):
    game_piece = canvas.create_oval(x, y, x + 50, y + 50, fill=color)
    game_pieces.append(game_piece)

# Create the Ludo game pieces
create_game_piece(150, 150, "red")
create_game_piece(300, 150, "blue")
create_game_piece(150, 300, "yellow")
create_game_piece(300, 300, "green")

# Create the dice button
dice_button = tk.Button(window, text="Roll Dice", width=10, height=2, font=("Arial", 12, "bold"))
dice_button.pack(pady=10)

# Create the dice result label
dice_result_label = tk.Label(window, text="Dice Result: ", font=("Arial", 12))
dice_result_label.pack()

# Function to roll the dice
def roll_dice():
    dice_result = random.randint(1, 6)
    dice_result_label.config(text="Dice Result: " + str(dice_result))
    move_game_piece(dice_result)

# Function to move a Ludo game piece
def move_game_piece(steps):
    selected_piece = random.choice(game_pieces)
    canvas.move(selected_piece, steps * 50, 0)

    if canvas.coords(selected_piece)[2] >= 400:
        canvas.delete(selected_piece)
        game_pieces.remove(selected_piece)
        check_game_over()

# Function to check if the game is over
def check_game_over():
    if len(game_pieces) == 0:
        messagebox.showinfo("Game Over", "All game pieces have reached the destination!")
        window.destroy()

# Bind the dice button to the roll_dice function
dice_button.config(command=roll_dice)

# Run the main window loop
window.mainloop()
