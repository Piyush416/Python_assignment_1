# Write a program to find the greatest common divisor (GCD) of two input numbers

# Code in Python:

a = int(input("Enter a 1st number: "))
b = int(input("Enter a 2nd number: "))

if a > b:
    result = b
else:
    result = a

while result:
    if a % result == 0 and b % result == 0:
        print(result)
        break
    result-=1

