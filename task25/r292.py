from fnmatch import fnmatch

for i in range(4329, 10**10, 4329):
    if fnmatch(str(i), '1*1298*6'):
        print(i, i // 4329)
