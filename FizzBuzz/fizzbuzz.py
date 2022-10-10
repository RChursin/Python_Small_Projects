# Project: FizzBuzz
"""
Instructions
Your program should print each number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
`When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
`And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
"""

# Solution 1
for number in range(1, 101):  # Loop through the numbers 1 to 100
    if number % 3 == 0 and number % 5 == 0:  # Check if the number is divisible by 3 and 5
        print("FizzBuzz")  # Print "FizzBuzz"
    elif number % 3 == 0:  # Check if the number is divisible by 3
        print("Fizz")  # Print "Fizz"
    elif number % 5 == 0:  # Check if the number is divisible by 5
        print("Buzz")  # Print "Buzz"
    else:  # If the number is not divisible by 3 or 5
        print(number)  # Print the number

# Solution 2
for number in range(1, 101):  # Loop through the numbers 1 to 100
    if number % 3 == 0:  # Check if the number is divisible by 3
        if number % 5 == 0:  # Check if the number is divisible by 5
            print("FizzBuzz")  # Print "FizzBuzz"
        else:  # If the number is not divisible by 5
            print("Fizz")  # Print "Fizz"
    elif number % 5 == 0:  # Check if the number is divisible by 5
        print("Buzz")  # Print "Buzz"
    else:  # If the number is not divisible by 3 or 5
        print(number)  # Print the number
