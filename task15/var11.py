for a in range(1, 1000):
    if all((x % a != 0) <= ((x % 24 == 0) <= (x % 96 != 0)) for x in range(1, 1000)):
        print(a)