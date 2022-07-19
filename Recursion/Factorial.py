def fact_rec(n):
    if n == 0:
        return 1
    return fact_rec(n-1) * n


n = int(input("Enter the number : "))
print((fact_rec(n)))
