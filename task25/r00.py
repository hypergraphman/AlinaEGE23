def f(n):
    res = {1, n}
    for d in range (2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


for i in range(194455, 194500 + 1):
    if len(f(i)) == 4:
        print(f(i))