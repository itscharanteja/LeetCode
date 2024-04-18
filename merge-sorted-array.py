def merge(n1, m, n2, n):
    for j in range(n):
        n1[m + j] = n2[j]
    n1.sort()


n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]
merge(n1, 3, n2, 3)
print(n1)
