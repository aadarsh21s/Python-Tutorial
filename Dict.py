dicto = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(dicto)
print(dicto["name"])  # Accessing value by key
print(dicto.get("age"))  # Accessing value using get() method
print(dicto.keys())  # Getting all keys
print(dicto.values())  # Getting all values
print(dicto.items())  # Getting all key-value pairs
print(len(dicto))  # Getting the number of key-value pairs
print("name" in dicto)  # Checking if a key exists

for key, value in dicto.items():
    print(f"{key}: {value}")  # Iterating through key-value pairs

#another way 
for key, value in dicto.items():
    print(f"The value corresponding to the key '{key}' is '{value}'")  # Iterating through key-value pairs


#Dictionary Methods
#Adding a new key-value pair
dicto["country"] = "USA"
print(dicto)    

#Updating an existing key-value pair
dicto["age"] = 31
print(dicto)

#Removing a key-value pair using pop()
removed_value = dicto.pop("city")
print(f"Removed value: {removed_value}")
print(dicto)

#Removing a key-value pair using popitem()
removed_item = dicto.popitem()
print(f"Removed item: {removed_item}")
print(dicto)

#Clearing the dictionary
dicto.clear()
print(dicto)

#Copying a dictionary
dicto_copy = dicto.copy()
print(dicto_copy)  # Output: {}

#Merging two dictionaries
dicto1 = {"a": 1, "b": 2}
dicto2 = {"b": 3, "c": 4}
dicto1.update(dicto2)
print(dicto1)  # Output: {'a': 1, 'b': 3, 'c': 4}   

