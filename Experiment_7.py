# Write a program to check if an input string is a palindrome


# Code in Python:

string = input("Enter a String: ")

rstring= string[::-1]

if rstring == string:
    print("true")
else:
    print("false")