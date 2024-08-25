import heapq
import sys
input = sys.stdin.readline

n = int(input())
min_q = []
max_q = []
current = int(input())
print(current)
for _ in range(n - 1):
    num = int(input())
    if num > current:
        heapq.heappush(max_q, num)
    else:
        heapq.heappush(min_q, -num)

    if len(min_q) > len(max_q):
        heapq.heappush(max_q, current)
        current = -heapq.heappop(min_q)
    elif len(max_q) > len(min_q) + 1:
        heapq.heappush(min_q, -current)
        current = heapq.heappop(max_q)
    print(current)
