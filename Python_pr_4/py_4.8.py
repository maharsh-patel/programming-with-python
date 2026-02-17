my_tuple = (10, 20, 30, 40, 50)

print("Original Tuple:", my_tuple)

temp = list(my_tuple)
temp.pop(2)
my_tuple = tuple(temp)

print("Tuple after removing 3rd element:", my_tuple)
