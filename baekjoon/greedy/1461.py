n, m = map(int, input().split())
pos = []
neg = []
numbers = []
result = 0

for num in map(int, input().split()):
    if num > 0:
        pos.append(num)
    else:
        neg.append(abs(num))
pos.sort(reverse=True)
neg.sort(reverse=True)


for i in range(len(pos)):
    if i % m == 0:
        result += pos[i] * 2
        numbers.append(pos[i])
for i in range(len(neg)):
    if i % m == 0:
        result += neg[i] * 2
        numbers.append(neg[i])
numbers.sort()
print(result - numbers[-1])