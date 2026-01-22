"""Write a program to check if number is Armstrong."""


num = int(input("Enter a number:-"))
sum =0
temp = num
while temp > 0:
    digit = temp%10
    sum = digit**3 + sum 
    temp = temp//10
if num == sum:
    print("The number", num, " is armstrong")
else:
    print("The number is not armstrong")
