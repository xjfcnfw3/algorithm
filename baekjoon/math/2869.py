a, b, v = map(int, input().split())
answer = 1
v = v - a
answer += v // (a - b)
if v % (a - b) != 0:
    answer += 1
print(answer)