from itertools import product

words = product('012345678', repeat=5)
res = set()
for w in words:
    if w[0] in '2468' and w[-1] not in '18' and w.count('3') <= 1:
        res.add(w)
print(len(res))
