"""Write a program to check special number. (Number is equal to the sum of its divisors)157"""


num = int(input("enter a number: "))

sum = 0
for i in range(1, num):
    if num%i == 0:
        sum = sum + i
if sum==num:
    print("The number", num, "is a special number")
else:
    print("The number", num, "is not a special number")

