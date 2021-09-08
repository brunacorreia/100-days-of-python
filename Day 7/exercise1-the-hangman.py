from hangman_img import logo, stages
import random
word_list = ["sort", "reverse", "remove", "pop", "insert", "add", "index", "extend", "count", "copy", "clear", "append", "isnumeric", "type", "upper", "lower"]

# randomly choose a word from the word_list
word = random.choice(word_list)

# to keep track of the remained chances
lives = 5
print(logo)
print("Welcome to the Python Handman Game. You have 5 chances to get the hidden Python Method, good luck!")

# blank spaces according to random word length
display = []
for letter in word:
    display.append('_')

while '_' in display:
    guess = input("Guess a letter to save the hangman: \n").lower()
    if guess in display:
        print(f"You've already guessed the letter {guess}.")

# to complete the blank spaces if the letter chosen by the user matches the word        
    for index, letter in enumerate(word):
        if letter == guess:
            display[index] = guess
# if chosen letter is not in word, chances are reduced and hangman is updated 
    if not guess in word:
        lives -= 1
        print(f"You've lost a life. There are {lives} chances left.")
        print(stages[lives])
    else:
        print(f"Correct! You guessed the letter '{guess}'!")
    
    if lives == 0:
        print(f"You lose. The Python Method was '{word}'. Try again later.")
        break

    # print at each correct stage, join the elements into a string separated by spaces
    print(f"{' '.join(display)}")

# if we have some lives left and we got rid of all the _ we win!
if lives != 0:
    print('You WIN!')

