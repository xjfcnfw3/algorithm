n = int(input())
result = 0


def check(num):
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True


for i in range(n, 1000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if check(i):
            result = i
            break

if result == 0:
    result = 1003001
print(result)
