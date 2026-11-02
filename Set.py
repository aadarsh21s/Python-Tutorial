info = {"unik", 1111, "python", 3.14, True}
print(info)

#To create a empty set
x= set()
print(type(x))

#Using loops
for val in info:
    print(val)

#Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
#Union
print(A | B)    
#or 
print(A.union(B))

#Intersection
print(A & B)
#or
print(A.intersection(B))

#Difference
print(A - B)
#or
print(A.difference(B))

#Symmetric Difference
print(A ^ B)    
#or
print(A.symmetric_difference(B))

#Adding elements to a set
A.add(6)
print(A)

#Removing elements from a set
A.remove(3)
print(A)

#update() method is used to add multiple elements to a set. It takes an iterable (like a list, tuple, or another set) as an argument and adds all the elements from that iterable to the set.
A.update([7, 8, 9])
print(A)  # Output: {1, 2, 4, 5, 6, 7, 8, 9}

#pop() method is used to remove and return an arbitrary element from the set. If the set is empty, it raises a KeyError.
removed_element = A.pop()
print(f"Removed element: {removed_element}")
print(A)  # Output: The set after removing an arbitrary element

#del() statement is used to delete the entire set. After using del, the set will no longer exist.
del A
# print(A)  # This will raise a NameError since A has been deleted  

#Discarding elements from a set
A.discard(10)  # This will not raise an error even if 10 is not present in the set
print(A)    

#Clearing a set
A.clear()
print(A)  # Output: set()

#Copying a set
B_copy = B.copy()
print(B_copy)  # Output: {4, 5, 6, 7, 8}

#isdisjoint() method is used to check if two sets have no elements in common. It returns True if the sets are disjoint, and False otherwise.
C = {9, 10}
print(A.isdisjoint(B))  # Output: True

#issubset() method is used to check if all elements of one set are present in another set. It returns True if the set is a subset, and False otherwise.
D = {4, 5}
print(D.issubset(B))  # Output: True

#issuperset() method is used to check if all elements of another set are present in the set. It returns True if the set is a superset, and False otherwise.
print(B.issuperset(D))  # Output: True

#len() function
print(len(B))  # Output: 5

#frozenset() function
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})

#for loop with set
for element in frozen_set:
    print(element)  # Output: 1 2 3 4 5 (each on a new line)    
    