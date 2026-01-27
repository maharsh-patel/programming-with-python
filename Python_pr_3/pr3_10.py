s = input("Enter main string: ")
sub = input("Enter substring: ")

found = False
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        found = True
        break   # break only when substring is found

if found:
    print("Substring is present")
else:
    print("Substring is not present")
