# # # SNAKE WATER GUN
# '''
#      Sanke = -1
#      Water = 0
#      Gun = 1
# '''


import tkinter as tk
from tkinter import messagebox
import random

def play_game(user_choice):
    choices = {"s": -1, "w": 0, "g": 1}
    rev_choices = {-1: "snake", 0: "water", 1: "gun"}

    computer_choice = random.choice([-1, 0, 1])
    user = choices[user_choice]

    result = ""
    if computer_choice == user:
        result = "Match draw! Hurray!"
    else:
        if computer_choice == -1 and user == 0:
            result = "You Lose!"
        elif computer_choice == -1 and user == 1:
            result = "You Win!"
        elif computer_choice == 0 and user == -1:
            result = "You Win!"
        elif computer_choice == 0 and user == 1:
            result = "You Lose!"
        elif computer_choice == 1 and user == 0:
            result = "You Win!"
        elif computer_choice == 1 and user == -1:
            result = "You Lose!"
        else:
            result = "Something went wrong."

    messagebox.showinfo("Result", f"Your choice: {rev_choices[user]}\nComputer choice: {rev_choices[computer_choice]}\n\n{result}")

def create_gui():
    root = tk.Tk()
    root.title("Snake Water Gun Game")
    root.geometry("300x200")

    label = tk.Label(root, text="Choose Snake, Water, or Gun", font=("Helvetica", 14))
    label.pack(pady=20)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    btn_snake = tk.Button(frame, text="Snake", width=10, command=lambda: play_game("s"))
    btn_snake.grid(row=0, column=0, padx=10)

    btn_water = tk.Button(frame, text="Water", width=10, command=lambda: play_game("w"))
    btn_water.grid(row=0, column=1, padx=10)

    btn_gun = tk.Button(frame, text="Gun", width=10, command=lambda: play_game("g"))
    btn_gun.grid(row=0, column=2, padx=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
