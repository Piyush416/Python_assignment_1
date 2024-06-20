# Write a program to check two strings are anagrams

# Code in Python:

string1 = input("Enter a 1st string: ")
string2 = input("Enter a 2nd string: ")

if sorted(string1) == sorted(string2):
    print("The string is anagram")
else:
    print("The string is Not anagram")
    
