import random
def calc_player2():
        return random.choice(lista)



print("Rock...")
print("Paper...")
print("Scissors...")
lista = (("rock", "scissors", "paper"))
player_wins = 0
computer_wins = 0

def in_game(player1, player2):
    if player1 == player2:
        print("It's a tie!")
        return 3
    elif ((player1 == "rock" and player2 == "scissors") or 
        (player1 == "paper" and player2 == "rock") or 
        (player1 == "scissors" and player2 == "paper")):
            print("player1 wins!!!") 
            return 0
    else:
        print("player2 wins!!!")
        return 1

while player_wins < 2 and computer_wins < 2:
    player1 = input("Player 1, make your move: ")
    if player1 not in lista:
        print("Something went wrong")
    else:
        player2 = calc_player2()
        print("Player2: " + player2)
        result = in_game(player1, player2)
        if int(result) == 0:
            player_wins+=1
        elif int(result) == 1:
            computer_wins+=1 


if player_wins > computer_wins:
    print (f"Ganaste! ({player_wins}/{computer_wins})")
else:
    print(f"Perdiste! ({player_wins}/{computer_wins})")