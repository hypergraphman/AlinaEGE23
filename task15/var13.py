for a in range(100):
    if all((x >= a) or (y >= a) or (x * y <= 200) for x in range(1, 100) for y in range(1, 100)):
        print(a)
