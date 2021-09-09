alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    converted_text = ""
    for letter in text:
        current_index = alphabet.index(letter)
        if direction == "encode":
            new_index = (current_index + shift) % 26
        elif direction == "decode":
            new_index = (current_index - shift) % 26
        else:
            print("Invalid command.")
        converted_text += alphabet[new_index]
    print(f"The {direction}d text is {converted_text}")
caesar(text, shift, direction)