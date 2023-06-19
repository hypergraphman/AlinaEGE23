# m == 2 ответы на 19
# m == 3 ответы на 20
# m == 4 ответы на 21
def f(s1, s2, c, m):
    # 129  в условии задачи
    if s1 + s2 >= 129:
        return c % 2 == m % 2
    if c == m:
        return False
    # ходы s + 1 и s * 2  в условии задачи
    h = [f(s1 + 1, s2, c + 1, m),
         f(s1 * 2, s2, c + 1, m),
         f(s1, s2 + 1, c + 1, m),
         f(s1, s2 * 2, c + 1, m),
         ]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# 100  в условии задачи
for s in range(1, 100):
    for m in range(1, 5):
        if f(6, s, 0, m):
            print(s, m)
            break