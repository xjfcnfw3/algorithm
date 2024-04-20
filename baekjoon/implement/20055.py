from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = deque(list(map(int, input().split())))
answer = 0
belt = deque([False] * N)
while True:
    answer += 1

    arr.rotate()
    belt.rotate()

    belt[N - 1] = False

    for i in range(N - 2, -1, -1):
        if belt[i] and not belt[i + 1] and arr[i + 1] > 0:
            belt[i], belt[i + 1] = False, True
            arr[i + 1] -= 1

    belt[N - 1] = False

    if arr[0] > 0:
        belt[0] = True
        arr[0] -= 1

    if arr.count(0) >= K:
        break
print(answer)