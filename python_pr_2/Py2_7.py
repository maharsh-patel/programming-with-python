"""
Question 7:
Write a Python program to count the number of odd
numbers from three given numbers and display the
maximum odd number.
"""


A = int(input("Enter 1sr number: "))
B = int(input("Enter 2nd number: "))
C = int(input("Enter 3rd number: "))

print("")

count = 0
max_odd = -1

if A%2!=0:
    count= count+1
    max_odd =A

if B % 2 !=0:
    count= count+1
    if max_odd < B:
        max_odd = B

if C % 2 !=0:
    count= count+1
    if max_odd < C:
        max_odd = C

print("Total odd numbers:", count)

if count>0:
    print("Maximum odd number:", max_odd)
else:
    print("no odd numbers")
