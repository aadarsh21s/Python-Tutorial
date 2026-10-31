#Nested If-Else Statements, Taking example of a student to determine if they have passed or failed based on their marks
# marks = int(input("Enter the student's marks: "))
# if marks >=90 and marks <=100:
#     print("Grade: A")
# elif marks >=80 and marks <90:
#     print("Grade: B")
# elif marks >=70 and marks <80:
#     print("Grade: C")
# elif marks >=60 and marks <70:  
#     print("Grade: D")
# else:
#     print("Grade: F")   

#Nested If-Else for negative and positive numbers
# num = int(input("Enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("The number is zero.")
#     else:
#         print("The number is positive.")
# else:
#     print("The number is negative.")

#Nested If-Else for checking if a number is even or odd
# num = int(input("Enter a number: "))
# if num >= 0:  
#     if num % 2 == 0:
#         print("The number is even.")
#     else: 
#         print("The number is odd.")

#Nested If-Else for checking if a number is prime or not
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("The number is not prime.")
#             break
#     else:
#         print("The number is prime.")
# else:
#     print("The number is not prime.")

#Nested If-Else for checking if a year is a leap year or not
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("The year is a leap year.")
# else:
#     print("The year is not a leap year.")

#Nested If-Else for checking if a number is divisible by another number
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num2 != 0:
#     if num1 % num2 == 0:
#         print("The first number is divisible by the second number.")
#     else:
#         print("The first number is not divisible by the second number.")
# else:
#     print("The second number cannot be zero.")

#Nested If-Else for checking if a character is a vowel or consonant
# char = input("Enter a character: ")
# if len(char) == 1 and char.isalpha():
#     if char.lower() in 'aeiou':
#         print("The character is a vowel.")
#     else:
#         print("The character is a consonant.")

#Nested If-Else Statements, Taking example of multiple subjects and their marks of a student to determine the grade
# Total_Subjects = 3
# marks = []
# for i in range(Total_Subjects):
#     mark = int(input(f"Enter marks for subject {i+1}: "))
#     marks.append(mark)

# total_marks = sum(marks)
# average_marks = total_marks / Total_Subjects    

# if average_marks >= 90:
#     print("Grade: A")
# elif average_marks >= 80:
#     print("Grade: B")
# elif average_marks >= 70:
#     print("Grade: C")
# else:
#     print("Grade: D")

