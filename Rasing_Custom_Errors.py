# This is a simple Python program that raises a custom error if the user inputs a number outside the specified range (5 to 10).
a = int(input("Enter a number: "))
if a < 5 or a > 10:
    raise ValueError("The number must be between 5 and 10.")

#attribute error
try:
    x = 10
    print(x.y)  # This will raise an AttributeError since 'int' object has no attribute 'y'.
except AttributeError as e:
    print(f"AttributeError: {e}")   

#float error
try:
    num = float("abc")  # This will raise a ValueError since "abc" cannot be converted to a float.
except ValueError as e:
    print(f"ValueError: {e}")

#Custom error class
class CustomError(Exception):
    """Custom exception class for specific error handling."""
    pass

