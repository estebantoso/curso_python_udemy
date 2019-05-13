# Guessing Game - 11/05/2019
from random import randint
cont = "y"

while not cont == "n":
    computer_num = randint(1, 10)
    win = False
    while not win:
        human_num = 0
        while not human_num in range(1, 11):
            human_num = int(input("Guess a number between 1 and 10: "))
        if human_num < computer_num:
            print("Too low, try again!")
        elif human_num > computer_num:
            print("Too high, try again!")
        else:
            print("YOU WIN!!!!")
            win = True
            cont = "n"
    cont = input("Do you want to keep playing? (y/n)")
    