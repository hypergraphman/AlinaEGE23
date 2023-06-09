s = open('r3.txt').read()

max_len = 0
cur_len = 0
for char in s:
    if char == 'EAB'[cur_len % 3]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    elif char == 'E':
        cur_len = 1
    else:
        cur_len = 0
print(max_len)