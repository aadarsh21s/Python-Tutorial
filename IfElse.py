# a= int(input("Enter your age: "))
# if a >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# #Printing the largest number among three numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1  

# #Printing the largest number among three numbers
# elif (num2 >= num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3  

# #printing the largest number
# print("The largest number is", largest) 

# #printing the smallest number among three numbers
# if (num1 <= num2) and (num1 <= num3):
#     smallest = num1
# elif (num2 <= num1) and (num2 <= num3):
#     smallest = num2
# else:
#     smallest = num3 

# #printing the smallest number
# print("The smallest number is", smallest)

# #Making a simple calculator using if else statements
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# print("Select operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# choice = input("Enter choice (1/2/3/4): ")
# if choice == '1':
#     print(num1, "+", num2, "=", num1 + num2)
# elif choice == '2':
#     print(num1, "-", num2, "=", num1 - num2)    
# elif choice == '3':
#     print(num1, "*", num2, "=", num1 * num2)
# elif choice == '4':
#     if num2 != 0:
#         print(num1, "/", num2, "=", num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid input")

# #Making a simple program to check if a number is positive, negative or zero
# num = float(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# elif num < 0:   
#     print("The number is negative.")
# else:
#     print("The number is zero.")    


# #Making a simple program to check if a number is even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.") 

#Making a simple program to check if a number is prime or not
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number.")
#             break
#     else:
#         print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")

#Single line if else statement
num = int(input("Enter a number: "))
# Using a single line if-else statement to check if the number is positive, negative, or zero
result = "positive" if num > 0 else "negative" if num < 0 else "zero"
print("The number is", result)

##Using a single line if-else statement to check if the number is even or odd
result = "even" if num % 2 == 0 else "odd"
print("The number is", result)

#Using a single line if-else statement to check if the number is prime or not
result = "prime" if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)) else "not prime"
print("The number is", result)