import random


# Create a function to generate a random number between a and b
def r(a=0.55, b=0.75):  # Define function and define numbers
    return random.uniform(a, b)  # Return numbers


# Create function to return random integers between a and b
def p(a=-3, b=3):  # Define function and define numbers
    return random.randint(a, b)  # Return integers
