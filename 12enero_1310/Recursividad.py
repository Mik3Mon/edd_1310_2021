def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

def printRev(n):
    if n > 0:
        printRev(n-1)
        print(n)

def fibonacci(n):
    if n == 1 or n == 0:
        return n
    if n > 1:
        return (fibonacci(n-1) + fibonacci(n-2))
