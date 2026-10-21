#Strings in Python
#Strings are sequences of characters enclosed in single quotes, double quotes, or triple quotes. In Python, strings are immutable, meaning they cannot be changed after they are created.
name="Adarsh"
learning="Python"

#Multi-line string
lrn= '''Hey,
My name is Adarsh and I am learning Python.'''

print(name)
print("Hey, My name is",name,"and I am learning",learning)
print(lrn)

print(name[0])  # Accessing the first character of the string
print(name[-1])  # Accessing the last character of the string
print(name[0:3])  # Accessing the first three characters of the string
print(name[::2])  # Accessing every second character of the string

#Length of the string
print("The length of the string is:", len(name))  # Length of the string

#Iterating through the string
print("Iterating through the string:")
for i in name:
    print(i)  # Printing each character of the string in a new line

#Uppercase and Lowercase
print("Uppercase:", name.upper())  # Converting the string to uppercase
print("Lowercase:", name.lower())  # Converting the string to lowercase

#Stripping whitespace
str_with_whitespace="   Hello, World!   "
print("Before stripping whitespace:", str_with_whitespace)
print("After stripping whitespace:", str_with_whitespace.strip())  # Stripping whitespace from the string

#Splitting and Joining
str_to_split="Hello,World,Python"
print("Before splitting:", str_to_split)
split_str=str_to_split.split(",")  # Splitting the string into a list
print("After splitting:", split_str)
joined_str=" ".join(split_str)  # Joining the list into a string
print("After joining:", joined_str)

#String Replacement
str_to_replace="Hello, World!"
print("Before replacement:", str_to_replace)
replaced_str=str_to_replace.replace("World", "Python")  # Replacing a substring
print("After replacement:", replaced_str)

#String Capatilization
str_to_capitalize="hello, world!"
print("Before capitalization:", str_to_capitalize)
capitalized_str=str_to_capitalize.capitalize()  # Capitalizing the first character of the string
print("After capitalization:", capitalized_str)

#String Counting
str_to_count="Hello, World! Hello, Python!"
print("Before counting:", str_to_count)
count_hello=str_to_count.count("Hello")  # Counting the occurrences of a substring
print("After counting:", count_hello)

#String Finding and indexing
str_to_find="Hello, World!"
print("Before finding:", str_to_find)
index_of_world=str_to_find.find("World")  # Finding the index of a substring
print("After finding:", index_of_world)
index_of_hello=str_to_find.index("Hello")  # Finding the index of a substring
print("After indexing:", index_of_hello)

#String endwith and startswith
str_to_check="Hello, World!"
print("Before checking:", str_to_check)
print("Does the string start with 'Hello'? :", str_to_check.startswith("Hello"))
print("Does the string end with 'World!'? :", str_to_check.endswith("World!"))  

#String formatting
age=20
print(f"My name is {name} and I am {age} years old.")  #Using f-string for string formatting


