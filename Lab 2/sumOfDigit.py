num = int(input("Enter a number: "))
sum = 0
while(num>0):
    sum = sum + (num % 10)
    num = num//10

print("The Sum of digits:",sum)