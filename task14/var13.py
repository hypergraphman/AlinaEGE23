for x in range(0, 15):
    n = (1 * 15**4 + 3 * 15**3 + 5 * 15**2 + x * 15 + 7 +
         7 * 15**4 + x * 15**3 + 5 * 15**2 + 3 * 15 + 1)
    if n % 14 == 0:
        print(n // 14)