def power(n,p):
    if p == 0:
        return 1
    return (n * power(n,p-1))

num = int(input("Enter the base: "))
pow = int(input("Enter the exponent: "))
print("The Power:",power(num,pow))