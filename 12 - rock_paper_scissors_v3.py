print("Rock...")
print("Paper...")
print("Scissors...")
lista = ["rock", "scissors", "paper"]

def in_game(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif ((player1 == "rock" and player2 == "scissors") or 
          (player1 == "paper" and player2 == "rock") or 
          (player1 == "scissors" and player2 == "paper")): 
        print("player1 wins!!!")
    else:
        print("player2 wins")


player1 = input("Player 1, make your move: ")
if player1 not in lista:
    print("Something went wrong")
else:
    player2 = input("Player 2, make your move: ")
    if player2 not in lista:
        print("Something went wrong")
    else:
        in_game(player1, player2)