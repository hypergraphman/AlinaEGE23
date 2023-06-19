for n in range(0, 10):
    s = '>' + 39 * '0' + n * '1' + 39 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>')
        if '>2' in s:
            s = s.replace('>2', '2>')
        if '>0' in s:
            s = s.replace('>0', '1>')
    print(n, sum(map(int, s[:-1])))