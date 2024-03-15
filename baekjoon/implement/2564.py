n, m = map(int, input().split())
t = int(input())
arr = []

def get_distance(a, b):
    if a == 1:
        return b
    elif a == 2:
        return n + m + n - b
    elif a == 3:
        return 2 * n + 2 * m - b
    return n + b

for _ in range(t):
    a, b = map(int, input().split())
    arr.append(get_distance(a, b))

user = list(map(int, input().split()))
user = get_distance(user[0], user[1])
answer = 0

for num in arr:
    answer += min(n * 2 + m * 2 - abs(user - num), abs(user - num))
print(answer)
