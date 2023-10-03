T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * (sum(arr) + 1)
    result = [0]
    for score in arr:
        for i in range(len(result)):
            if not visited[result[i] + score]:
                visited[result[i] + score] = True
                result.append(result[i] + score)
    print("#{} {}".format(test_case, len(result)))