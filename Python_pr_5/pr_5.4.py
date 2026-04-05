students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}
print("Names having 'a': ") 
for group in students.values():
    for name in group:
        if 'a' in name.lower():
            print(name)
