for y in range(0, 100):
    line = '>' + '1' * 16 + '2' * y + '3' * 16
    while '>1' in line or '>2' in line or '>3' in line:
        line = line.replace('>1', '1>', 1)
        line = line.replace('>2', '3>', 1)
        line = line.replace('>3', '1>', 1)
    print(y, sum(map(int, line[:-1])))