import bisect
t = int(input())

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_sum = []
b_sum = []
answer = 0
for i in range(n):
    temp = a[i]
    a_sum.append(temp)
    for j in range(i + 1, n):
        temp += a[j]
        a_sum.append(temp)
for i in range(m):
    temp = b[i]
    b_sum.append(temp)
    for j in range(i + 1, m):
        temp += b[j]
        b_sum.append(temp)
a_sum.sort()
b_sum.sort()
for i in range(len(a_sum)):
    l = bisect.bisect_left(b_sum, t - a_sum[i])
    r = bisect.bisect_right(b_sum, t - a_sum[i])
    answer += r - l
print(answer)