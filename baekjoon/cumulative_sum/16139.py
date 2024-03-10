import sys
input = sys.stdin.readline
s = input()
t = int(input())
d = dict()

def generate_cumulative_sum(s, c):
    arr = [0]
    temp = 0
    for i in range(len(s)):
        if s[i] == c:
            temp += 1
        arr.append(temp)
    return arr

for _ in range(t):
    a, i, j = input().split()
    if a not in d:
        d[a] = generate_cumulative_sum(s, a)
    print(d[a][int(j) + 1] - d[a][int(i)])
