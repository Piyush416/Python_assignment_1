# Write a program to check if an input year is a leap year


# Code in Python:

n = int(input("Enter a Year: "))

if n%400==0 or (n%100 != 0 and n%4 == 0):
    print(f"{n} is a Leap Year")
else:
    print(f"{n} is not a Leap Year")