n = input()
n = int(n)
x, y = [1, 1]
arr = input().split()

for a in arr:
    if a == 'L':
        if y > 1:
            y -= 1

    elif a == 'R':
        if y < n:
            y += 1

    elif a == 'D':
        if x < n:
            x += 1
    elif a == 'U':
        if x > 1:
            x -= 1

print(x, y)