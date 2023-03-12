n = 150
s = 0
while n > 1:
    s += n % 10
    n //= 10
print(s)