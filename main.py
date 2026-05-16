import random

def main():
    options = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")

    player = input("Enter rock, paper, or scissors: ").lower()

    computer = random.choice(options)

    if player not in options:
        print("Error: invalid input. Please choose rock, paper, or scissors.")
        return

    print("Computer chose:", computer)

    if player == computer:
        print("Result: It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("Result: You win!")
    else:
        print("Result: You lose!")

main()