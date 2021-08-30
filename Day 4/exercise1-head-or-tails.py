import random

def start_game():
    random_side = random.randint(0, 1)
    print(random_side)
    my_choice = int(input("Choose '0' for HEADS or '1' for TAILS\n"))
    if my_choice == random_side:
        restart_game = input("You got it CORRECT! Would you like to try again? 'Y' or 'N'?").lower()
        if restart_game == "y":
            start_game()
    else:
        restart_game = input("You got it wrong. Better luck next time. Would you like to try again? 'Y' or 'N'?").lower()
        if restart_game == "y":
            start_game()

start_game()

