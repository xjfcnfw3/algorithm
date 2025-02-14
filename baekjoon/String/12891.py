from collections import deque

s, p = map(int, input().split())

data = list(input())

a, c, g, t = map(int, input().split())

left, right = 0, p - 1

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

arr = deque(data[left:right])

for ch in arr:
    dic[ch] += 1
answer = 0

while right < s:
    dic[data[right]] += 1

    if dic["A"] >= a and dic["C"] >= c and dic["G"] >= g and dic["T"] >= t:
        answer += 1

    dic[data[left]] -= 1
    left += 1
    right += 1
print(answer)
