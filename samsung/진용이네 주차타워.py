from collections import deque

def check():
    for i in range(len(store)):
        if not store[i]:
            return i
    return -1

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    r = [int(input()) for _ in range(n)]
    w = [int(input()) for _ in range(m)]
    store = [False] * n
    cars = dict()
    q = deque()
    visited = []
    result = 0
    for _ in range(2 * m):
        car = int(input())
        if car > 0:
            idx = check()
            if idx > -1:
                store[idx] = True
                result += w[car - 1] * r[idx]
                cars[car] = idx
            else:
                q.append(car)
        else:
            idx = cars[-1 * car]
            store[idx] = False
            if q:
                rest_car = q.popleft()
                result += w[rest_car - 1] * r[idx]
                store[idx] = True
                cars[rest_car] = idx
    print("#{} {}".format(test_case, result))