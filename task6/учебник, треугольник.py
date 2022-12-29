count = 0
for x in range(1, 112):
    for y in range(1, 112):
        if x / 3 ** 0.5 < y < -x / 3 ** 0.5 + 111:
            count += 1
print(count)
