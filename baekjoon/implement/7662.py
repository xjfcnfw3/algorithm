import heapq
import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    max_q = []
    min_q = []
    m = int(input())
    visited = [False] * m
    for i in range(m):
        commend, num = input().split()
        if commend == 'I':
            heapq.heappush(max_q, (-int(num), i))
            heapq.heappush(min_q, (int(num), i))
            visited[i] = True
        elif commend == "D":
            if num == "1":
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)
            else:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    if max_q and min_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print("EMPTY")