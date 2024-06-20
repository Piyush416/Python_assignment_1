# Write a program to find the sum of digits of an input number

# Code in Python:

n = int(input("Enter a Number: "))

ans = 0
while n!=0:
    ans = ans + n%10
    n = n//10
    
print(ans)