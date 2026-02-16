numbers = [12, 45, 7, 89, 23, 56]

print("List:", numbers)

element = int(input("Enter element to search: "))

if element in numbers:
    print("Element found in list")
else:
    print("Element not found")

print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
