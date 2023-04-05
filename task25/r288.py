from fnmatch import fnmatch

for i in range(1, 10**8,1):
    if fnmatch (str(i), '1?58*129'):
        if i % 117 == 0 and i % 119 != 0 and i % 121 != 0:
            print(i, i // 117)
        elif i % 117 != 0 and i % 119 == 0 and i % 121 != 0:
            print(i, i // 119)
        elif i % 117 != 0 and i % 119 != 0 and i % 121 == 0:
            print(i, i // 121)