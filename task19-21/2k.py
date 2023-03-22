w = 69
start = 5

def f(a, b, c, m):
    if a + b >= w:
        return c % 2 == m % 2
    # if s > 72: return c % 2 != m % 2 - с верхним ограничением
    if c == m:
        return False
    moves = [f(a + 1, b, c + 1, m), f(a * 2, b, c + 1, m), f(a, b + 1, c + 1, m), f(a, b * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)  # any, если первый ход пети был неудачный


for i in range(1, w - start):
    for m in range(1, 5):
        if f(start, i, 0, m):
            print(i, m)
            break

