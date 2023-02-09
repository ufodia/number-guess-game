import random

def guess_the_number():
    # Welcome message
    print("Welcome to the Number Guessing Game!")
    
    # Input for lower bound of the range
    lower_bound = int(input("Enter the lower bound of the range: "))
    
    # Input for upper bound of the range
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Input for maximum number of tries
    tries_ = int(input("Enter the max tries: "))
    
    # Information about the number to be guessed
    print(f"I have generated a random number between {lower_bound} and {upper_bound}. Can you guess it in {tries_} tries or less?")
    
    # Generating the random number
    number = random.randint(lower_bound, upper_bound)
    
    # Initializing the number of tries
    tries = 0
    
    # Loop for guessing the number
    while tries < (tries_):
        # Input for the guess
        guess = int(input("Enter your guess: "))
        
        # Incrementing the number of tries
        tries += 1
        
        # Check if the guess is lower than the lower bound
        if guess < lower_bound:
            print(f"please write a number equal or higher than {lower_bound} ")
            tries -= 1
        # Check if the guess is higher than the upper bound
        elif guess > upper_bound:
            print(f"please write a number lower than {upper_bound}")   
            tries -= 1
        # Check if the guess is equal to the number
        elif guess == number:
            print(f"Congratulations! You have guessed the number in {tries_} tries.")
            return
        # Check if the guess is lower than the number
        elif guess < number:
            print("The number is higher.")
        # If none of the above conditions are met, the guess must be higher than the number
        else:
            print("The number is lower.")
    
    # If the maximum number of tries is reached
    print(f"Sorry, you have reached the maximum number of tries. The number was {number}.")

# Call to the function to start the game
guess_the_number()
exitus = input("Press enter to close the program: ")
