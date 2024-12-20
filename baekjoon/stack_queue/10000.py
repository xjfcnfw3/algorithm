import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a + b, 2 * b))
arr.sort()
q = []
result = 1

for end, dist in arr:
    last = end
    offset = False
    start = end - dist
    while q:
        e, s = heapq.heappop(q)
        e = -e
        if e <= start:
            heapq.heappush(q, (-e, s))
            break
        if e != last and start <= s:
            continue
        if start <= s:
            last = s
        if last == start:
            offset = True
    result += 1
    if offset:
        result += 1
    heapq.heappush(q, (-end, start))

print(result)