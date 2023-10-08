from collections import deque
T = 10

for test_case in range(1, T + 1):
    n = input()
    arr = map(int, input().split())
    q = deque(arr)
    count = 1
    while True:
        num = q.popleft()
        num -= count
        count += 1
        if count > 5:
            count = 1
        if num <= 0:
            q.append(0)
            break
        q.append(num)
    print("#" + str(n), end = " ")
    q = list(q)
    for num in range(len(q)):
        if num == len(q) -1:
            print(q[num])
        else:
            print(q[num], end = " ")