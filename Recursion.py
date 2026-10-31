#Python Recursive Function
def factorial(n) :
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
print(factorial(4))

# Python Recursive Function for Fibonacci
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Find the nth Fibonacci number:
print(fibonacci(5))  # Output: 5
print(fibonacci(6))  # Output: 8

#Another Example
terms = 10

print(f"Fibonacci sequence (first {terms} terms):")
for i in range(terms):
    print(fibonacci(i), end=" ")

