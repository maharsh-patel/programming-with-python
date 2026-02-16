numbers = [12, 45, 7, 89, 23, 56]

print("List:", numbers)

element = int(input("Enter element to search: "))

found = False
for i in numbers:
    if i == element:
        found = True
        break

if found:
    print("Element found in list")
else:
    print("Element not found")

max_val = numbers[0]
min_val = numbers[0]

for i in numbers:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum value:", max_val)
print("Minimum value:", min_val)
