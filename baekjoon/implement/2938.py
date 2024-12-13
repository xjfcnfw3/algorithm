from collections import deque
n = int(input())
arr = list(map(int, input().split()))

queues = [deque(), deque(), deque()]

for num in arr:
    queues[num % 3].append(num)

if len(queues[0]) > (n + 1) / 2 or (not queues[0] and queues[1] and queues[2]):
    print(-1)
    exit(0)
result = []
while queues[1]:
    if len(queues[0]) > 1:
        result.append(queues[0].popleft())
    result.append(queues[1].popleft())

if queues[0]:
    result.append(queues[0].popleft())

while queues[2]:
    result.append(queues[2].popleft())
    if queues[0]:
        result.append(queues[0].popleft())

print(*result)