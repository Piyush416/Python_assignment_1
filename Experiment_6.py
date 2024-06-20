# Write a program to generate the Fibonacci sequence up to a given number of terms

# Code in Python:

n = int(input("Enter a Number: "))
num1 = -1 
num2 = 1
count=1

while count<=n:
    ans = num1+num2
    print(ans,end=" ")
    num1 = num2
    num2 = ans
    count+=1
        