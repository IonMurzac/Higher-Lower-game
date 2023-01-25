# Import necessary libraries
import random

# Initialize the flag for if the user wants to play
is_user_action = True

# While loop for the game
while is_user_action:
    # Get the user's choice to play
    user_selection = input("Would you like to play Higher - Lower? Yes 'y' or No 'n':")
    if user_selection == "y":
        
        # Initialize the number of attempts
        attempts = 0

        # Generate a random number between 1 and 100
        random_number = random.randint(1, 100)

        # While loop for the guessing game
        while is_user_action:
            # Increment the number of attempts
            attempts += 1

            # Get the user's guess
            user_number = int(input("Please enter your number: "))

            # Check if the user's guess is too low
            if user_number < random_number:
                print("Your number is HIGHER!")

            # Check if the user's guess is too high
            elif user_number > random_number:
                print("Your number is LOWER!")

            # Check if the user's guess is correct
            elif user_number == random_number:
                print(f"Correct, the number is {random_number}.")
                break
            
            # Check if the user has reached the maximum number of attempts
            if attempts == 10:
                print(f"You lose!! Corect number was {random_number}.")
                break
    
    # If the user does not want to play
    elif user_selection == "n":
        print(" Good Bye!")
        break