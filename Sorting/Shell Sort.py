def shell_sort(A):
    n = len(A)
    gap = n//2
    while gap > 0:
        i = gap
        while i < n:
            temp = A[i]
            j = i - gap
            while j >= 0 and A[j] > temp:
                A[j+gap] = A[j]
                j = j - gap
            A[j + gap] = temp
            i += 1
        gap //= 2


A = [9, 5, 2, 6, 8 ]
print("Original Arrays: ", A)
shell_sort(A)
print("Sorted Array: ", A)
