def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the value of n: "))
if n <= 0:
        print("invalid input")
else:
    for i in range(1,n+1):
        print(fibonacci(i), end=" ")