#List Comprehension

marks = [ 35, 45, 55, "Unik", True]
print(marks[0])
print(len(marks)-3)
print(marks[1:3])
print(marks[::2])
print(marks[-1])
print(marks[1:4:2])
print(marks)


if 45 in marks:
    print("Number 45 is present in the list")
else:
    print("Number 45 is not present in the list")


lst = [i*i for i in range(1, 11)]
print(lst)
lst1 = [i*i for i in range(1, 11) if i%2==0]
print(lst1)


#list comprehension with nested loops
lst2 = [i*j for i in range(1, 4) for j in range(1, 4)]
print(lst2)

#list comprehension with nested loops and if condition
lst3 = [i*j for i in range(1, 4) for j in range(1, 4) if i*j%2==0]
print(lst3)

#List comprehension with nested loops and if-else condition
lst4 = [i*j if i*j%2==0 else i+j for i in range(1, 4) for j in range(1, 4)]
print(lst4)

#List comprehension with nested loops and if-elif-else condition
lst5 = [i*j if i*j%2==0 else i+j if i+j%2==0 else i-j for i in range(1, 4) for j in range(1, 4)]
print(lst5)

#List comprehension with nested loops and if-elif-else condition and multiple if conditions
lst6 = [i*j if i*j%2==0 else i+j if i+j%2==0 else i-j if i-j%2==0 else i*j+i+j for i in range(1, 4) for j in range(1, 4)]
print(lst6)

#List Methods
print("\n List Methods:")
lst7 = [1, 2, 3, 4, 5]
lst7.append(6)  # Adding an element to the end of the list
print(lst7)
lst7.insert(2, 10)  # Inserting an element at a specific index
print(lst7)
lst7.remove(3)  # Removing an element from the list
print(lst7)
lst7.pop()  # Removing the last element from the list
print(lst7) 
lst7.pop(1)  # Removing an element at a specific index
print(lst7)
lst7.sort()  # Sorting the list in ascending order
print(lst7)
lst7.sort(reverse=True)  # Sorting the list in descending order
print(lst7)
lst7.reverse()  # Reversing the list
print(lst7)
lst7.clear()  # Clearing the list
print(lst7)
lst8 = [1, 2, 3, 4, 5]
print(lst8.count(2))  # Counting the occurrences of an element in the list
lst8.extend([6, 7, 8])  # Extending the list with another list
print(lst8)
lst9 = [1, 2, 3, 4, 5]
print(lst9.index(3))  # Finding the index of an element in the list

#To copy a list, we can use the copy() method or the list() constructor.
lst10 = [1, 2, 3, 4, 5]
lst11 = lst10.copy()  # Copying a list using the copy() method
print(lst11)
lst12 = list(lst10)  # Copying a list using the list() constructor
print(lst12)