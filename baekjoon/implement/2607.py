n = int(input())
first = list(input())
result = 0

for _ in range(n - 1):
    target = first[:]
    cnt = 0
    for c in input():
        if c in target:
            target.remove(c)
        else:
            cnt += 1
    if cnt < 2 and len(target) < 2:
        result += 1
print(result)