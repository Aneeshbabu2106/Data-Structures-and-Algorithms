def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        pos = i
        while pos > 0 and A[pos - 1] > cvalue:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = cvalue


A = [9, 4, 3, 7, 1]
print("Original Arrays: ", A)
insertion_sort(A)
print("Sorted Array: ", A)
