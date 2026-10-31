#Tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
tuple1 = ("apple", "banana", "cherry")
print(tuple1)

#Accessing tuple items
print(tuple1[1])  # Accessing the second item of the tuple
print(tuple1[2])  # Accessing the third item of the tuple
print(tuple1[-1])  # Accessing the last item of the tuple
print(tuple1[0:2])  # Accessing the first two items of the tuple
print(tuple1[::2])  # Accessing every second item of the tuple
print(tuple1[-2:])  # Accessing the last two items of the tuple
print(tuple1[:-2])  # Accessing all items of the tuple except the last two
print(tuple1[::-1])  # Accessing the items of the tuple in reverse order
print(len(tuple1))  # Length of the tuple
print(type(tuple1))  # Type of the tuple
print(tuple1.count("apple"))  # Counting the occurrences of an item in the tuple
print(tuple1.index("banana"))  # Finding the index of an item in the tuple
print("Iterating through the tuple:")
for i in tuple1:
    print(i)  # Printing each item of the tuple in a new line

print(tuple1[1:2:2])  # Accessing the second item of the tuple with step 2


#Changing tuple values
#Tuples are unchangeable, meaning that you cannot change, add, or remove items

#Check if "apple" is present in the tuple
if "apple" in tuple1:
    print("Yes, 'apple' is in the tuple")

#Tuple methods
tuple2 = (1, 2, 3, 4, 5)
print(tuple2)  # Printing the tuple
print(tuple2.count(2))  # Counting the occurrences of an item in the tuple
print(tuple2.index(3))  # Finding the index of an item in the tuple 
print("Iterating through the tuple:")
for i in tuple2:
    print(i)  # Printing each item of the tuple in a new line

#Joining tuples
tuple3 = (6, 7, 8)
tuple4 = tuple2 + tuple3  # Joining two tuples
print(tuple4)  # Printing the joined tuple  

#Changing a tuple to a list and back to a tuple
tuple5 = (1, 2, 3, 4, 5)
list1 = list(tuple5)  # Changing the tuple to a list
list1.append(6)  # Adding an item to the list
list1.pop(0)  # Removing the first item from the list
list1[0] = 10  # Changing the first item of the list
tuple6 = tuple(list1)  # Changing the list back to a tuple
print(tuple6)  # Printing the new tuple

#Unpacking a tuple
tuple7 = ("apple", "banana", "cherry")
#Unpacking the tuple into variables
fruit1, fruit2, fruit3 = tuple7
print(fruit1)  # Printing the first variable
print(fruit2)  # Printing the second variable
print(fruit3)  # Printing the third variable    


