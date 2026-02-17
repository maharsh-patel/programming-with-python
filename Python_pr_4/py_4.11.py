import re

mobile = input("Enter mobile number: ")

pattern = "^[6-9][0-9]{9}$"

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
