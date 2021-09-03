#Step 1 
import random
word_list = ["sort", "reverse", "remove", "pop", "insert", "add", "index", "extend", "count", "copy", "clear", "append"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

life = 5
print("Welcome to the Python Handman Game. You have 5 chances to get the hidden Python Method, good luck!")
while life > 0:
    guess = input("Guess a letter to save the hangman: \n")

    if guess in word:
        all_guesses = []
        all_guesses += guess
        all_guesses = str(all_guesses)
        print(f"Correct! Letters you've guessed: {all_guesses}")
    else:
        life -= 1
        print(f"You've lost a life. There are {life} chances left.")
    if guess == word:
        print("YOU WIN")
if life == 0:
    print(f"GAME OVER. The Python Method was '{word}'. Try again later.")


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
'''
def chances_left():
    life = 5
    while life > 0:
        if guess in word:
            print("Correct!")
        else:
            life -= 1
            print("You've lost one life.")
            user_guess()
    if life == 0:
        print("GAME OVER")
'''