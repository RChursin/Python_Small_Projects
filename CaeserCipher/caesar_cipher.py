# Code Challenge: Caesar Cipher
"""
Instructions
You are going to write a program that encrypts a message using the Caesar Cipher. This is a substitution cipher where
each letter of the original message is shifted a certain number of places down the alphabet.
e.g. plain_text = "hello"
shift = 5
cipher_text = "mjqqt"
print output: "The encoded text is mjqqt"
e.g. plain_text = "mjqqt"
shift = -5
cipher_text = "hello"
print output: "The decoded text is hello"

Important: Notice how the cipher_text changes when the shift value is either positive or negative. This is because the
direction of shift changes when the shift value is negative.

Important: The cipher only encrypts letters. All other characters should remain as they are. e.g. plain_text = "meet me at 3"
shift = 1
cipher_text = "nffu nf bu 3"
print output: "The encoded text is nffu nf bu 3"
e.g. plain_text = "nffu nf bu 3"
shift = -1
cipher_text = "meet me at 3"
print output: "The decoded text is meet me at 3"
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']  # Create a list of the alphabet and assign it to a variable called alphabet.

# Create a function called caesar that takes two inputs, text and shift, and that returns the encoded text.


def caesar(start_text, shift_amount, cipher_direction):  # Create a function to encrypt or decrypt the message
    end_text = ""  # Create a variable to store the encrypted or decrypted message
    if cipher_direction == "decode":  # Check if the user wants to decrypt the message
        shift_amount *= -1  # If the user wants to decrypt the message, make the shift amount negative
    for char in start_text:  # Loop through each character in the message
        if char in alphabet:  # Check if the character is in the alphabet
            position = alphabet.index(char)  # Get the index of the character in the alphabet
            new_position = position + shift_amount  # Add the shift amount to the index of the character
            end_text += alphabet[new_position]
        else:  # If the character is not in the alphabet
            end_text += char  # Add the character to the encrypted or decrypted message
    print(f"The {cipher_direction}d text is {end_text}")


# Completed the function to encrypt or decrypt the message
should_end = False  # Create a variable to check if the program should end
while not should_end:  # Loop until the user enters 'yes' or 'no'
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  # Ask the user if they want to encrypt
    # or decrypt a message
    text = input("Type your message:\n").lower()  # Ask the user to type in a message
    shift = int(input("Type the shift number:\n"))  # Ask the user to type in a shift number

    shift = shift % 26  # If the shift amount is greater than 26, then the shift amount should be set to the remainder
    # of the shift amount divided by 26.

    # Call the function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to restart the program
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "yes":  # Check if the user entered 'yes'
        should_end = False  # If the user entered 'yes', set should_end to False
    elif restart == "no":  # Check if the user entered 'no'
        should_end = True
        print("Goodbye")
    else:
        print("Invalid input")
