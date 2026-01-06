"""
Question 5:
Write a Python program to check whether a given
character is a vowel or not.
"""


ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Not a vowel")



ch = input("Enter a character: ")

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' \
   or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("Vowel")
else:
    print("Not a vowel")
