# Write a program to find the least common multiple (LCM) of two input numbers

# Code in Python:

a = int(input("Enter a 1st number: "))
b = int(input("Enter a 2nd number: "))

i = 2
while i:
    if i%a == 0 and i%b == 0:
        print(i)
        break
    i+=1
