numbers = [64, 25, 12, 22, 11]

print("Original List:")
print(numbers)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("Sorted List (Without Built-in):")
print(numbers)
