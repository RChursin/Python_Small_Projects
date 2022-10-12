# Project: Secret Auction
"""
Instructions
You are going to write a program that will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the `choice()` function.


Example Input
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
bid = [100, 200, 300, 400, 500, 600]

Example Output
Freddie is the winner of the secret auction with a bid of $600.
"""

bids = {}  # Create a dictionary to store the bids
bidding_finished = False  # Create a variable to store whether the bidding has finished


def find_highest_bidder(bidding_record):  # Create a function to find the highest bidder
    highest_bid = 0  # Create a variable to store the highest bid
    winner = ""  # Create a variable to store the winner
    for bidder in bidding_record:  # Loop through the bidding record
        bid_amount = bidding_record[bidder]  # Get the bid amount
        if bid_amount > highest_bid:  # Check if the bid amount is higher than the highest bid
            highest_bid = bid_amount  # Set the highest bid to the bid amount
            winner = bidder  # Set the winner to the bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")  # Print the winner


while not bidding_finished:  # Loop until the bidding has finished
    name = input("What is your name? ")  # Get the user's name
    bid = int(input("What is your bid? $"))  # Get the user's bid
    bids[name] = bid  # Add the user's name and bid to the dictionary
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")  # Ask if there are any other bidders
    if should_continue == "no":  # Check if there are any other bidders
        bidding_finished = True  # Set the bidding_finished variable to True
        find_highest_bidder(bids)  # Find the highest bidder
    elif should_continue == "yes":  # Check if there are any other bidders
        bidding_finished = False  # Set the bidding_finished variable to False
    else:  # If the user enters anything other than 'yes' or 'no'
        print("Invalid input. Please try again.")  # Print an error message


