a=input("Enter a value: ")
b=input("Enter another value: ")
print("You entered:",a)
print("You also entered:",b)
print("Sum of a and b:",int(a)+int(b))  # This will add the numbers since we convert them to integers

print("Now let's see what happens if we don't convert them to integers:")
print("Sum of a and b without conversion:",a+b)  # This will concatenate the strings since they are not converted to integers  

print("Now let's see what happens if we convert them to floats:")
print("Sum of a and b as floats:",float(a)+float(b))  # This will add the numbers as floats since we convert them to floats

print("Now let's see what happens if we convert them to strings:")
print("Sum of a and b as strings:",str(a)+str(b))  # This will concatenate the strings since we convert them to strings

print("Now let's see what happens if we convert them to complex numbers:")
print("Sum of a and b as complex numbers:",complex(a)+complex(b))  # This will add the numbers as complex numbers since we convert them to complex numbers

print("Now let's see what happens if we convert them to booleans:")
print("Sum of a and b as booleans:",bool(a)+bool(b))

print("Now let's see what happens if we convert them to bytes:")
print("Sum of a and b as bytes:",bytes(a, 'utf-8')+bytes(b, 'utf-8'))  # This will concatenate the bytes since we convert them to bytes
