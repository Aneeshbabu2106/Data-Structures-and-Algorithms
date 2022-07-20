def linearsearch(A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index += 1
    return -1


A = [55, 99, 88, 33]
found = linearsearch(A, 55)
print("Result : ", found)
