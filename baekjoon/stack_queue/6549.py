import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        break
    result = 0
    stk = []
    for i in range(len(arr)):
        if not stk:
            stk.append((i, arr[i]))
            continue

        if stk[-1][1] <= arr[i]:
            stk.append((i, arr[i]))
        else:
            while len(stk) > 0 and stk[-1][1] > arr[i]:
                temp = stk.pop()
                if len(stk) == 0:
                    width = i - 1
                else:
                    width = i - stk[-1][0] - 1
                result = max(result, temp[1] * width)
            stk.append((i, arr[i]))
    while stk:
        temp = stk.pop()
        if len(stk) == 0:
            width = arr[0]
        else:
            width = arr[0] - stk[-1][0]
        result = max(result, temp[1] * width)
    print(result)

