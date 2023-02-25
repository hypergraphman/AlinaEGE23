from itertools import product

for i, word in enumerate(product('aoy', repeat=5), start=1):
    word = ''.join(word)
    if i == 240:
        print(word)