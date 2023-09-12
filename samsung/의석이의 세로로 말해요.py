from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    arr = deque([deque(list(input())) for _ in range(5)])
    result = ""
    while arr:
        q = arr.popleft()
        result += q.popleft()
        if q:
            arr.append(q)
    print("#{} ".format(test_case), end = "")
    print("".join(result))
