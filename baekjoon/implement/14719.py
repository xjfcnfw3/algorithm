h, w = map(int, input().split())
arr = list(map(int, input().split()))
water = 0
for i in range(1, h+1):
    stack = []
    hole = 0
    for j in range(0, w):
        if i <= arr[j]:
            top = 0
            if stack:
                top = stack[-1]
            stack.append(1)
            if stack and top == 0:
                water += hole
                hole = 0
        else:
            if stack:
                hole += 1
                stack.append(0)
print(water)
