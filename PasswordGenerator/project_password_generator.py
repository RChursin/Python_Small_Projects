# Project: Password Generator

"""
Instructions
You are going to write a program that automatically generates a secure password for the user.
e.g.
4-letter word + 4 digit number = JduE&2020
e.g.
6-letter word + 2 digit number = xxE[AQ83
e.g.
5-letter word + 3 digit number = g^2jk8&P

Extension
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random  # Import the random module
print("Welcome to the PyPassword Generator!")  # Print welcome message
symbol = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^",
          "_", "`", "{", "|", "}", "~"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
# Eazy Level - Order not randomised:
# e.g. 4 letter word + 4 digit number = JduE&2020
password = ""  # Create a variable to store the password
for i in range(4):  # Loop through the letters
    password += random.choice(letters)  # Add a random letter to the password
for i in range(4):  # Loop through the numbers
    password += random.choice(numbers)  # Add a random number to the password
print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter word + 4 digit number = g^2jk8&P
import random  # Import the random module
password = ""  # Create a variable to store the password
for i in range(4):  # Loop through the letters
    password += random.choice(letters)  # Add a random letter to the password
for i in range(4):  # Loop through the numbers
    password += random.choice(numbers)  # Add a random number to the password
password = list(password)  # Convert the password to a list
random.shuffle(password)  # Shuffle the password
password = "".join(password)  # Convert the password back to a string
print(password)

# Interactive with user Solution:
import random  # Import the random module
print("Welcome to the PyPassword Generator!")  # Print welcome message
user_input = input("How strong do you want your password to be? Type 'easy' or 'hard': ")  # Ask the user how strong they want their password to be
password = ""  # Create a variable to store the password
if user_input == "easy":  # Check if the user input is easy
    for i in range(4):  # Loop through the letters
        password += random.choice(letters)  # Add a random letter to the password
    for i in range(4):  # Loop through the numbers
        password += random.choice(numbers)  # Add a random number to the password
elif user_input == "hard":  # Check if the user input is hard
    for i in range(4):  # Loop through the letters
        password += random.choice(letters)  # Add a random letter to the password
    for i in range(4):  # Loop through the numbers
        password += random.choice(numbers)  # Add a random number to the password
    password = list(password)  # Convert the password to a list
    random.shuffle(password)  # Shuffle the password
    password = "".join(password)  # Convert the password back to a string
print(password)

# Interactive with user Solution 2:
import random  # Import the random module
print("Welcome to the PyPassword Generator!")  # Print welcome message
user_input_letters = int(input("How many letters would you like in your password? "))  # Ask the user how many letters they want in their password
user_input_numbers = int(input("How many numbers would you like in your password? "))  # Ask the user how many numbers they want in their password
user_input_symbols = int(input("How many symbols would you like in your password? "))  # Ask the user how many symbols they want in their password

password = ""  # Create a variable to store the password
for i in range(user_input_letters):  # Loop through the letters
    password += random.choice(letters)  # Add a random letter to the password
for i in range(user_input_numbers):  # Loop through the numbers
    password += random.choice(numbers)  # Add a random number to the password
for i in range(user_input_symbols):  # Loop through the symbols
    password += random.choice(symbol)  # Add a random symbol to the password
password = list(password)  # Convert the password to a list
random.shuffle(password)  # Shuffle the password
password = "".join(password)  # Convert the password back to a string
print(password)

# Example 1:
import random
# Create a list of words
words = ["aardvark", "baboon", "camel"]
# Create a list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a list of symbols
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
# Choose a random word from the list
word = random.choice(words)
# Choose a random number from the list
number = random.choice(numbers)
# Choose a random symbol from the list
symbol = random.choice(symbols)
# Combine the word, number and symbol to create a password
password = word + str(number) + symbol
# Print the password
print(password)
# Output: aardvark2*


# Example 2:
import random
# Create a list of words
words = ["aardvark", "baboon", "camel"]
# Create a list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a list of symbols
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
password_list = []
# Choose a random word from the list
word = random.choice(words)
password_list.append(word)
# Choose a random number from the list
number = random.choice(numbers)
password_list.append(str(number))
# Choose a random symbol from the list
symbol = random.choice(symbols)
password_list.append(symbol)
# Combine the word, number and symbol to create a password
password = "".join(password_list)
# Print the password
print(password)
# Output: aardvark2*

# Example 3:
import random
# Create a list of words
words = ["aardvark", "baboon", "camel"]
# Create a list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create a list of symbols
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
password_list = []
# Choose a random word from the list
word = random.choice(words)
password_list.append(word)
# Choose a random number from the list
number = random.choice(numbers)
password_list.append(str(number))
# Choose a random symbol from the list
symbol = random.choice(symbols)
password_list.append(symbol)
# Shuffle the password list
random.shuffle(password_list)
# Combine the word, number and symbol to create a password
password = "".join(password_list)
# Print the password
print(password)
# Output: aardvark2*

