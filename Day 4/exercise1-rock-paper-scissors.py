import random

computer_guess = random.randint(1, 3)
print(computer_guess)
player1 = input("Your time. Type '1' for ROCK, '2' for PAPER or '3' for SCISSORS.")


'''
rock = 1
paper = 2
scissors = 3
'''


def start_game():
    your_score = 0
    computer_score = 0
    if player1 == "1":
        if computer_guess == 1:
            print("The computer has chosen ROCK. It's a draw.")
        elif computer_guess == 2:
            print("The computer has chosen PAPER. You loose! :(")
            computer_score += 1
        elif computer_score == 3:
            print("YOU WIN.")
            your_score += 1
    elif player1 == "2":
        if computer_guess == 2:
            print("The computer has chosen PAPER. It's a draw.")
        elif computer_guess == 3:
            print("The computer has chosen SCISSORS. You loose! :(")
            computer_score += 1
        elif computer_score == 3:
            print('YOU WIN.')
            your_score += 1
    elif player1 == "3":
        if computer_guess == 3:
            print("The computer has chosen SCISSORS. It's a draw.")
        elif computer_guess == 1:
            print("The computer has chosen PAPER. You loose! :( ")
            computer_score += 1
            return computer_score
        elif computer_guess == 2:
            print('YOU WIN.')
            your_score += 1
            return your_score
    if your_score == 5 or computer_score == 5:
        if your_score > computer_score:
            restart_game = input(f"Final score: \n PLAYER 1: {your_score} - COMPUTER: {computer_score}. You WIN the game. Would you like to play again? Type 'Y' or 'N'").lower()
            if restart_game == "Y":
                start_game()
        else:
            restart_game = input(f"Final score: \n PLAYER 1: {your_score} - COMPUTER: {computer_score}. You LOSE. Would you like to play again? Type 'Y' or 'N'").lower()
            if restart_game == "Y":
                start_game()
start_game();
