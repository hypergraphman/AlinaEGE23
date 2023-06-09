s = open('test.txt').read()

max_len = 0
cur_len = 0
for char in s:
    if char in 'ABC':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0
print(max_len)