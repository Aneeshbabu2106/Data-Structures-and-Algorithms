def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if A[j] < A[position]:
                position = j
        temp = A[i]
        A[i] = A[position]
        A[position] = temp


A = [2, 8, 4, 3, 7]
print("Original list: ", A)
selection_sort(A)
print("Sorted list : ", A)

