import sys
from collections import deque
input = sys.stdin.readline

def double(n):
    return n * 2 % 10000


def sub(n):
    return (n - 1) % 10000


def right(n):
    return n % 10 * 1000 + n // 10


def left(n):
    return n % 1000 * 10 + n // 1000

def bfs(num):
    global b
    q = deque()
    q.append((num, ""))
    answer = ""
    visited = [False for _ in range(10001)]
    visited[num] = True
    while q:
        n, result = q.popleft()
        if n == b:
            answer = result
            break
        d = double(n)
        if not visited[d]:
            visited[d] = True
            q.append((d, result + "D"))
        s = sub(n)
        if not visited[s]:
            visited[s] = True
            q.append((s, result + "S"))

        l = left(n)
        if not visited[l]:
            q.append((l, result + "L"))
            visited[l] = True

        r = right(n)
        if not visited[r]:
            visited[r] = True
            q.append((r, result + "R"))
    return answer


for _ in range(int(input())):
    a, b = map(int, input().split())
    answer = []
    print(bfs(a))
