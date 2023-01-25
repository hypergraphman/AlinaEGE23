from itertools import product

count = 0
for word in product('ВЕСНА', repeat=3):
    word = ''.join(word)
    if word.count('А') >= 1:
        print(word)
        count += 1
print(count)