T = int(input())
result = []
for test_case in range(1, T + 1):
    n = input()
    while len(n) != 1:
        arr = map(int, list(n))
        n = str(sum(arr))
    result.append(n)
for i in range(len(result)):
    print("#{} {}".format(i + 1, result[i]))