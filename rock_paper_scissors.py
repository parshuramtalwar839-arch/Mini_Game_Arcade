# Mini Game Arcade - Rock Paper Scissors
# Beginner Python project using input, conditions, loops and random.

import random

choices = ["rock", "paper", "scissors"]

print("================================")
print("      ROCK PAPER SCISSORS")
print("================================")
print("First to 3 points wins!")
print("Type rock, paper, or scissors.")
print("Type quit whenever you want to stop.")

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player = input("\nYour choice: ").lower().strip()

    if player == "quit":
        print("Thanks for playing!")
        break

    if player not in choices:
        print("Please enter rock, paper, scissors, or quit.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score = player_score + 1
    else:
        print("Computer wins this round!")
        computer_score = computer_score + 1

    print("Score -> You:", player_score, "| Computer:", computer_score)

if player_score == 3:
    print("\nCongratulations! You won the game.")
elif computer_score == 3:
    print("\nComputer won the game. Better luck next time!")

print("Final score -> You:", player_score, "| Computer:", computer_score)
