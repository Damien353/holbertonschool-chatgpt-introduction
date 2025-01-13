#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculates the factorial of a given number n using recursion.

    Parameters:
    n (int): The number for which to calculate the factorial.

    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1  # Factorial of 0 is defined as 1
    else:
        return n * factorial(n-1)  # Recursively calculate the factorial

# Convert the first command-line argument to an integer and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)

