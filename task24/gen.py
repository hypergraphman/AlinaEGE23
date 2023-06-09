from random import choice

f = open('r3.txt', 'w')
for _ in range(1000000):
    f.write(choice('ABCDE'))
