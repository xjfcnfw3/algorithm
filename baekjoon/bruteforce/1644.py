import math
n = int(input())
result = 0
numbers = []
visited = [False] * (n + 1)
visited[1], visited[0] = True, True
if 1 == n:
    print(0)
    exit(0)
for i in range(2, int(math.sqrt(n)+1)):
    if not visited[i]:
        j = 2

        while (i * j) <= n:
            visited[i*j] = True
            j += 1
for i in range(2, n + 1):
    if not visited[i]:
        numbers.append(i)
left, right = 0, 0
s = numbers[0]

while left <= right:
    if s >= n:
        if s == n:
            result += 1
        s -= numbers[left]
        left += 1
    else:
        right += 1
        if right >= len(numbers): break
        s += numbers[right]
print(result)