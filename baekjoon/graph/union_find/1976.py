n = int(input())
m = int(input())

cities = [0] * (n + 1)
for i in range(n + 1):
    cities[i] = i


def find(num):
    if cities[num] != num:
        cities[num] = find(cities[num])
    return cities[num]


for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] == 0:
            continue
        a = find(i)
        b = find(j + 1)
        if a < b:
            cities[b] = a
        else:
            cities[a] = b
arr = list(map(int, input().split()))
root = cities[arr[0]]
for i in range(1, m):
    if cities[arr[i]] != root:
        print("NO")
        exit(0)
print("YES")
