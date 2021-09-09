alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift %= 26

def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for letter in plain_text:
        current_index = alphabet.index(letter)
        new_index = current_index + shift_amount
        encrypted_text += alphabet[new_index]
    print(f"The encoded text is {encrypted_text}")

def decrypt(encrypted_text, shift_amount):
    plain_text = ""
    for letter in encrypted_text:
        current_index = alphabet.index(letter)
        new_index = current_index - shift_amount
        plain_text += alphabet[new_index]
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(encrypted_text=text, shift_amount=shift)