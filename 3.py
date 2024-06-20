# Write a program to calculate the factorial of a given number

# Code in Python:

n = int(input("Enter a Number: "))

def fact(n):
    # base case
    if n == 0:
        return 1
    ans = n * fact(n-1)
    return ans

print(f"Factorial of {n} number is: {fact(n)}")