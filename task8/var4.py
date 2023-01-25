from itertools import product

count = 0
for word in product('АЗЛОПЬ', repeat=6):
    word = ''.join(word)
    count += 1
    if word.count('Ь') <= 1 and word.count('А') == 1 and word.count('З') <= 2:
        print(count, word)