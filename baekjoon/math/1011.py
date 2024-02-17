n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    distance = b - a
    current = 0
    move = 1
    result = 0
    while current < distance:
        result += 1
        current += move
        if result % 2 == 0:
            move += 1
    print(result)
