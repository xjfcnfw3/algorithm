arr = []
T = int(input())

for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    result = min(b, d) - max(a, c)
    result = result if result > 0 else 0
    arr.append(result)
for i in range(len(arr)):
    print("#{} {}".format(i + 1, arr[i]))
