def binary_search_rec(A, key, l, r):
    if l > r:
        return -1
    mid = (l+r)//2
    if A[mid] == key:
        return mid
    elif A[mid] > key:
        return binary_search_rec(A, key, l, mid-1)
    elif A[mid] < key:
        return binary_search_rec(A, key, mid+1, r)


A = [10, 20, 30, 40]
found = binary_search_rec(A,30,0,len(A))
print("Result : ", found)
