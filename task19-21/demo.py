# m == 2 ответы на 19
# m == 3 ответы на 20
# m == 4 ответы на 21
def f(s, c, m):
    # 129  в условии задачи
    if s >= 129:
        return c % 2 == m % 2
    if c == m:
        return False
    # ходы s + 1 и s * 2  в условии задачи
    h = [f(s + 1, c + 1, m),
         f(s * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# 129  в условии задачи
for s in range(1, 129):
    for m in range(1, 5):
        if f(s, 0, m):
            print(s, m)
            break