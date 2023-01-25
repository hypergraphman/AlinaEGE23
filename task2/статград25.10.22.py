from itertools import permutations

print('x y z w f')
a = []
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:

                f = (w <= (y == z)) and (y == (z <= x))
                a.append([x, y, z, w, int(f)])
print(a)
xyzw = 'xyzw'
for i1, i2, i3, i4 in permutations([0, 1, 2, 3]):
    print(xyzw[i1], xyzw[i2], xyzw[i3], xyzw[i4])
