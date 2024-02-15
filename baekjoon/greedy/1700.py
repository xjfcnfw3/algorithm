from collections import Counter
import heapq

n, k = map(int, input())
arr = list(map(int, input().split()))
q = []
result = 0
current = 0
con = []
for k, v in Counter(arr):
    heapq.heappush(q, (k, v))

for i in range(k):
    if current < n:
        con.a
