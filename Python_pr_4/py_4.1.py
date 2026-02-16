my_list = ["Maharsh Patel", "23CE123", 20, "CE", "First Class"]

print("Original List:")
print(my_list)

my_list.insert(2, "Ganpat University")
print("\nAfter Insert:")
print(my_list)

my_list.append("Semester 4")
print("\nAfter Append:")
print(my_list)

extra_data = ["Python", "PR-4"]
my_list.extend(extra_data)
print("\nAfter Extend:")
print(my_list)

my_list[3] = 21
print("\nAfter Update:")
print(my_list)

my_list.remove("PR-4")
print("\nAfter Remove:")
print(my_list)
