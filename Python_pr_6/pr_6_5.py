def listAdd(a, b):
    result = []
    
    for i in range(len(a)):
        result.append(a[i] + b[i])
    
    return result


A = listAdd([1,2,3], [1,2,3])

print(A)
