from itertools import product

words = product('01234567', repeat = 5)
res = set()
for w in words:
    word = ''.join(w)
    if (word.count('6') == 1 and '16' not in word and '61' not in word and
                                 '36' not in word and '63' not in word and
                                 '56' not in word and '65' not in word and
                                 '76' not in word and '67' not in word and word[0] != '0'):
        res.add(word)
print(len(res))