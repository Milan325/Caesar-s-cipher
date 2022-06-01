alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
signs = [".", ",", "?", "!", ":", ";", " "]
direction = input("Write \"encode\" for encoding or \"decode\" for decoding: ").lower()
text_input = input("Your text: ").lower()
moving_rate = int(input("How many places you want to move your letters? "))


def encrypt(text, change):
    ciphered = ""
    for letter in text:
        if letter in signs:
            ciphered += letter
        else:
            position = alphabet.index(letter)
            new_position = position + change
            new_letter = alphabet[new_position]
            ciphered += new_letter
    return ciphered


def decrypt(text, change):
    deciphered = ""
    for letter in text:
        if letter in signs:
            deciphered += letter
        else:
            position = alphabet.index(letter)
            new_position = position - change
            new_letter = alphabet[new_position]
            deciphered += new_letter
    return deciphered


if direction == "encode":
    print(f"Your word is ciphered as: {encrypt(text=text_input, change=moving_rate)}")
elif direction == "decode":
    print(f"Your word is deciphered as: {decrypt(text=text_input, change=moving_rate)}")
else:
    print("Error, check your input")
