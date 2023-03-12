from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2:
        return f(n - 1) + f(n - 2)


for i in range(1, 1006):
    f(i)

print((f(1006) - f(1004)) // f(1005))
