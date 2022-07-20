def binary_search (A, key):
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = (l+r)//2
        if A[mid] == key:
            return mid
        elif A[mid] > key:
            r = mid - 1
        elif A[mid] < key:
            l = mid + 1
    return -1


A = [20, 30, 40, 50]
found = binary_search(A, 50)
print("Result :", found)
