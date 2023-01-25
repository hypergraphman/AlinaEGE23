def treug(n, m, k):
    return max(n, m, k) < n + m + k - max(n, m, k)


for a in range(1, 1000):
    if all(not ((treug(x, 12, 20) == (not (max(x, 5) > 28))) and treug(x, a, 3)) for x in range(1, 1000)):
        print(a)