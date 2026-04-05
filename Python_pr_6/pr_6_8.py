data = [
    {"name": "Maharsh", "age": 20},
    {"name": "Amit", "age": 19},
    {"name": "Neha", "age": 25}
]

# sorting based on age
data_sorted = sorted(data, key=lambda x: x["age"])

print("Sorted list:")
for i in data_sorted:
    print(i)
