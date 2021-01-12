from Recursividad import factorial,printRev,fibonacci

print("Prueba Factorial")
for num in range(1,11,1):
    r = factorial(num)
    print(f"El factorial de {num} es {r}")

print("\nPrueba printRev")

printRev(3)

print("\nPrueba Fibonacci")

for num in range(11):
    print(str(fibonacci(num)) + "," , end = "")
