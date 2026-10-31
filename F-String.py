
letter = "Hey, my name is {} and I am from {}"
country = "Nepal"
name = "Adarsh"
print(letter.format(name, country))  # Using format() method for string formatting
#Using f-string to format the string
#another way to format the string using f-string
formatted_string = f"Hey, my name is {name} and I am from {country}"
print(formatted_string) 


#F-String with expressions
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}")

#For decimal formatting, we can use the format specifier inside the f-string.
pi = 3.141592653589793
print(f"The value of pi is approximately {pi:.2f}")  # Formatting to 2 decimal places

#F-String with dictionary
person = {"name": "Adarsh", "age": 20}
print(f"My name is {person['name']} and I am {person['age']} years old.")  # Accessing dictionary values inside f-string    

#F-String with list
fruits = ["apple", "banana", "cherry"]
print(f"My favorite fruits are {fruits[0]}, {fruits[1]}, and {fruits[2]}.")  # Accessing list elements inside f-string  

#F-String with nested expressions
x = 5
y = 10
print(f"The product of {x} and {y} is {x * y}, and the sum is {x + y}.")  # Using nested expressions inside f-string    

