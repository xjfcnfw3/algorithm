n = int(input())
result = 0
def check(num):
    return num + sum(list(map(int, str(num))))


for i in range(1, n + 1):
    if check(i) == n:
        result = i
        break
print(result)