import sys
input = sys.stdin.readline
MAX_NUM = 1000000

result = [1] * (MAX_NUM + 1)
answer = [0] * (MAX_NUM + 1)
answer[1] = 1

for i in range(2, MAX_NUM + 1):
    temp = 1
    while i * temp <= MAX_NUM:
        result[i * temp] += i
        temp += 1
    answer[i] = answer[i - 1] + result[i]

n = int(input())
for _ in range(n):
    sys.stdout.write(str(answer[int(input())])+"\n")