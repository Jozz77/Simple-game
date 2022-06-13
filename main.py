# Program make a simple Rock-Paper-Scissors game

#Imports Random Module
from optparse import Option
import random





  # Welcome Message
print("Starting the Rock-Paper-Scissors game...")
print("Rules of the game: Rock beats Scissors, Paper beats Rock, Scissors beats Paper")
print("So choose wisely....")
print("And the game begins")
print("Enter R for Rock, P for Paper and S for Scissors")



while True:
# Defines the two players
    play = ["R", "P", "S"]
    computer_player = random.choice(play)
    # Let the game begin
    user_input = input('Choose R, P or S: ')

    
    if user_input in play:
        print('Your choice is ', user_input)
        print('Computer choosed ', computer_player)

        if user_input == computer_player:
            print('Its a tie, Nobody wins')
            continue

        if user_input == "S" and computer_player == "R":
            print('Player (Scissors): CPU (Rock)')
            print('Computer wins')
        elif user_input == "R" and computer_player == "S":
            print('Player (Rock): CPU (Scissors)')
            print('You win')

        elif user_input == "R" and computer_player == "P":
            print('Player (Rock): CPU (Paper)')
            print('Computer wins')
        elif user_input == "P" and computer_player == "R":
            print('Player (Paper): CPU (Rock)')
            print('You win')

        elif user_input == "P" and computer_player == "S":
            print('Player (Paper): CPU (Scissors)')
            print('Computer wins')
        elif user_input == "S" and computer_player == "P":
            print('Player (Scissors): CPU (Paper)')
            print('You win')
        break
    else:
        print('Invalid Input')


    