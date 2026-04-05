# Step 1: Create dictionary
d1 = {"a": 1, "b": 2, "c": 3, "d": 4}

# 1) Print values of a, d, and c
print("Value of a:", d1["a"])
print("Value of d:", d1["d"])
print("Value of c:", d1["c"])

# 2) Calculate and print sum of all values
total = d1["a"] + d1["b"] + d1["c"] + d1["d"]
print("Sum of all values:", total)

# 3) Add new key-value pair (e,5)
d1["e"] = 5
print("Updated dictionary:", d1)
