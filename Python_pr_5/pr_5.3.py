d = {"a": 1, "b": 2, "c": 3, "d": 5}

filtered_d = {}

for key, value in d.items():
    if value <= 2:
        filtered_d[key] = value

print(filtered_d)
