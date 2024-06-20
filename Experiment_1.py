# Write a program to check is a given number is
# even or odd
# positive, negative or zero


# Code in Python:
n = int(input("Enter a Number: "))

# Odd and even check number
if n % 2 == 0:
    print("The Number is Even")
else:
    print("The Number is Odd")
    
# Check the number is positive or negative or zero
if n > 0:
    print("Number is Positive")
elif n<0:
    print("Number is Negative")
else:
    print("Number is Zero")