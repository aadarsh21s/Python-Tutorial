a = input("Enter a number for multiplication: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:                                         #We can also use = except Exception as e:  print(e)
    print("Invalid Input!")

#Another example of exception handling
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
except ZeroDivisionError:            #ZeroDivisionError is a specific exception that occurs when you try to divide a number by zero. By catching this exception, we can provide a more user-friendly error message instead of letting the program crash.
    print("Error: Division by zero is not allowed.")
except ValueError:                   #ValueError is another specific exception that occurs when a function receives an argument of the right type but an inappropriate value. In this case, it would occur if the user inputs a non-numeric value when prompted for a number. By catching this exception, we can inform the user that their input was invalid and prompt them to enter numeric values instead.
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:               #This is a general exception handler that will catch any other exceptions that are not specifically handled by the previous except blocks. The variable e will contain information about the exception that occurred, which can be useful for debugging or logging purposes.
    print(f"An unexpected error occurred: {e}")
except IndentationError:  #This is a specific exception that occurs when there is an indentation error in the code. Indentation errors can happen if the code is not properly aligned or if there are inconsistent spaces or tabs used for indentation. By catching this exception, we can provide feedback to the user about the indentation issue.
    print("Error: There is an indentation error in the code.")

#Finally block is used to execute code that must run regardless of whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.
finally:
    print("Execution completed.")

