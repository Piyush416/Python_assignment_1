# Write a program to check if an input number is prime or not

# Code in Python:

n = int(input("Enter a Number: "))

i = 2
while n > i:
    if n % i == 0:
        print(f"{n} is not a prime number")
        exit()
    i+=1
print(f"{n} is a prime number")