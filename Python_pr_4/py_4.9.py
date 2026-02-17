courses = ("JAVA", "PHP", "C#", "Android")

print("Original Tuple:", courses)

temp = list(courses)

temp.insert(2, "HTML")
temp.insert(3, "Python")

courses = tuple(temp)

print("Updated Tuple:", courses)
