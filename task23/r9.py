def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    return f(s + 1, e) + f(s * 2, e)


print(f(1, 10) * f(10, 20))
