import heapq, sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) < n:
        while len(arr) < n:
            arr += list(map(int, input().split()))
    left_q = []
    right_q = []
    result = []
    for i in range(n):
        if len(left_q) == len(right_q):
            heapq.heappush(left_q, -arr[i])
        else:
            heapq.heappush(right_q, arr[i])

        if right_q and -left_q[0] > right_q[0]:
            a = -heapq.heappop(left_q)
            b = heapq.heappop(right_q)
            heapq.heappush(right_q, a)
            heapq.heappush(left_q, -b)
        if i % 2 == 0:
            result.append(-left_q[0])
    print(len(result))
    print(*result)
