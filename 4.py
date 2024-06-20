# Write a program to find factors of a given number
# Code in Python:

n = int(input("Enter a Number: "))

i = 1
while i!=n+1:
    if n % i == 0:
        print(i,end=",")
    i+=1
    