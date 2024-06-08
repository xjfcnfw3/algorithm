
year = [0] * 21
death = [0] * 21
n = int(input())
year[1] = 1
death[4] = 1

for i in range(2, n + 1):
    birth = year[i - 1]
    year[i] = year[i - 1] * 2 - death[i]
    if i % 2 == 0:
        if i + 4 <= 20:
            death[i + 4] += birth
    else:
        if i + 3 <= 20:
            death[i + 3] += birth
print(year[n])