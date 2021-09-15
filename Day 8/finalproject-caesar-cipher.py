from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    converted_text = ""
    for char in text:
        if char in alphabet:
            current_index = alphabet.index(char)
            if direction == "encode":
                new_index = (current_index + shift) % 26
            elif direction == "decode":
                new_index = (current_index - shift) % 26
            else:
                print("Invalid command.")
            converted_text += alphabet[new_index]
        else:
            converted_text += char
    print(f"The {direction}d text is '{converted_text}'")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to try it again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_end = True
        print("Goodbye.")
