import sys
input = sys.stdin.readline

n, h = map(int, input().split())
up = [0] * (h + 1)
down = [0] * (h + 1)

for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1
answer = n
answer_count = 0

for i in range(h - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

for i in range(1, h + 1):
    if answer > (down[i] + up[h - i + 1]):
        answer = down[i] + up[h - i + 1]
        answer_count = 1
    elif answer == down[i] + up[h - i + 1]:
        answer_count += 1
print(answer, answer_count)