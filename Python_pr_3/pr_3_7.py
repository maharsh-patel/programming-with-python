str = input("enter a string: ")
length = 0
uppercase = 0 
lowercase = 0

for char in str: 
    length +=1
    if char.isupper():
        uppercase += 1
    
    elif char.islower():
        lowercase += 1


print("Length of string:", length)
print("Number of uppercase letters:", uppercase)
print("Number of lowercase letters:", lowercase)