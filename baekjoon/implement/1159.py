n = int(input())
initial = dict()
for i in range(n):
    player = input()
    a = player[0]
    if a not in initial:
        initial[a] = 1
    else:
        initial[a] += 1
result = []
for i in initial:
    if initial[i] >= 5:
        result.append(i)
result.sort()
if result:
    print("".join(result))
    exit()
print("PREDAJA")