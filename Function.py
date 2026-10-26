# def CalculateGmean(a, b):
#     return (a + b) / 2

# gmean = CalculateGmean(9, 1)
# print(gmean)



# def IsGreater(a, b):
#     if a>b:
#         print(a, "which is a is greater than", b)
#     else:
#         print(b, "which is b is greater than", a)

# IsGreater(4,5)



# # pass function is used when we want to create a function but we don't want to write any code in it. It is used as a placeholder for future code.
# def PlaceholderFunction():
#     pass



#Default arguments are used when we want to give a default value to a parameter in a function. If the user does not provide a value for that parameter, the default value will be used.
def Greet(name="Guest"):
    print("Hello", name)

Greet("Alice")
Greet()


#Keyword arguments are used when we want to provide values to parameters in a function by specifying the parameter name. This allows us to provide values to parameters in any order.
def Introduce(name, age):
    print("My name is", name, "and I am", age, "years old.")    

Introduce(name="Alice", age=25)
Introduce(age=30, name="Bob")

#Variable-length arguments are used when we want to pass a variable number of arguments to a function.
def Sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(Sum(1, 2, 3, 4, 5))

#Required arguments are used when we want to provide values to parameters in a function without specifying the parameter name. The values will be assigned to the parameters in the order they are provided.
def Multiply(a, b):
    return a * b    

print(Multiply(5, 6))

#taking tuples as arguments in a function
def average(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)

#Taking dictionaries as arguments in a function
def print_student_info(**student):
    for key, value in student.items():
        print(key + ":", value)
        