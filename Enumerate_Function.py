#Enumerate function is used to add a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using the list() method.

for index, value in enumerate(['apple', 'banana', 'cherry']):
    print(index, value)

    print("The index of", value, "is", index)

#Another example of using enumerate function with a list of numbers
numbers = [10, 20, 30, 40, 50]
for index, value in enumerate(numbers):
    print("The index of", value, "is", index)

#Another example using marks
marks = [85, 90, 78, 92, 88]
for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Awasome! You have scored the third highest mark:", mark)