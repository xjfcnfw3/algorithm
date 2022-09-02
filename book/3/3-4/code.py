n, k = map(int, input().split())
num = 0
while True:
    if n % k == 0:
        n = n/k
        num += 1
    else:
        n -= 1
        num += 1
    if n == 1:
        break
print(num)