#Explicit Type Casting
#what is explcit type casting in python
#Explicit type casting is the process of converting a variable from one data type to another data type using built-in functions. In Python, you can use functions like int(), float(), str(), etc., to explicitly convert data types.
a=1
b=23
print("Before Type Casting:")
print("Value of a:",a)
print("Type of a:",type(a))
print("Value of b:",b)  
print("Type of b:",type(b))

c="1"
d="23"
print("After Type Casting:")
print("Value of c:",c)
print("Type of c:",type(c))
print("Value of d:",d)
print("Type of d:",type(d))
print("Sum of c and d:",int(c) + int(d))  # Type casting from string to integer

#Implicit Type Casting
#What is implicit type casting in python
#Implicit type casting, also known as type coercion, is the automatic conversion of a variable
x=10
y=3.14
print("Before Implicit Type Casting:")
print("Value of x:",x)
print("Type of x:",type(x))
print("Value of y:",y)
print("Type of y:",type(y))
print("After Implicit Type Casting:")
print("Value of x:",x)
print("Type of x:",type(x))
print("Value of y:",y)
print("Type of y:",type(y))
print("Sum of x and y:",x + y)  # Implicit type casting from integer to float
