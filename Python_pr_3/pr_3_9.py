st = input("Enter string: ")
i = int(input("Enter index: "))

new_str = "" 
for index in range(len(st)): 
    if index != i: 
        new_str += st[index] 
print("Modified string:", new_str) 
