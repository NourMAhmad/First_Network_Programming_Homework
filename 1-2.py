def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))

print("The factorial of", number, "is" ,factorial_iterative(number))

