import sys

input = sys.stdin.readline

t = int(input())
s = set()

for _ in range(t):
    arr = input().strip().split()

    if len(arr) == 1:
        if arr[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()

    else:
        operation, x = arr[0], arr[1]
        x = int(x)

        if operation == "add":
            s.add(x)
        elif operation == "remove":
            s.discard(x)
        elif operation == "check":
            print(1 if x in s else 0)
        elif operation == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)