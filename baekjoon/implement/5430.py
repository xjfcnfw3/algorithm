from collections import deque

t = int(input())


for _ in range(t):
    commend = list(input())
    n = int(input())
    q = deque(input()[1:-1].split(','))
    reverse = 0
    error = False
    if n == 0:
        q = deque()

    for c in commend:
        if c == "R":
            reverse += 1
        else:
            if not q:
                print("error")
                error = True
                break
            if reverse % 2 == 0:
                q.popleft()
            else:
                q.pop()
    if not error:
        if reverse % 2 != 0:
            q.reverse()
            print("[" + ",".join(q) + "]")
        else:
            print("[" + ",".join(q) + "]")
