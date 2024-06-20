# Write a program to calculate the sum of the first N natural numbers

# Code in Python:
n = int(input("Enter a number: "))
ans = 0
while n!=0:
    ans = ans+n
    n-=1

print(ans)