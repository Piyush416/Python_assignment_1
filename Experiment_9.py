# Write a program to check if an input number is an Armstrong number

# Code in Python:

n = int(input("Enter a Number: "))

oNumber = n
count=0
while n!=0:
    n = n//10
    count+=1
    
n = oNumber

ans = 0
while n!=0:
    l = n%10
    ans = ans + pow(l,count)
    n = n//10

if oNumber == ans:
    print(f"{oNumber} is ArmStrong Number")
else:
    print(f"{oNumber} is Not ArmStrong Number")

    