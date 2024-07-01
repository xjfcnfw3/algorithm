n = int(input())

a = n // 5
b = 0

while a >= 0:
    temp = n - 5 * a
    if temp % 3 == 0:
        b = temp // 3
        break
    a -= 1
if a:
    print(a + b)
elif n % 3 == 0:
    print(n // 3)
else:
    print(-1)