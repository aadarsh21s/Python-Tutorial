
letter = "Hey, my name is {} and I am from {}"
country = "Nepal"
name = "Adarsh"
#Using f-string to format the string
print(letter.format(name, country))  # Using format() method for string formatting

#another way to format the string using f-string
formatted_string = f"Hey, my name is {name} and I am from {country}"
print(formatted_string) 
