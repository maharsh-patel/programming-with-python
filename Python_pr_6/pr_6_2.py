def check_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


n = int(input("Enter value of n: "))

print("Prime numbers are:")

for i in range(1, n+1):
    if check_prime(i):
        print(i, end=" ")
