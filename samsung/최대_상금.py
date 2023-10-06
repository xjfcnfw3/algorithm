def dfs(count):
    global result
    if not count:
        result = max(result, int("".join(num)))
        return
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]

            if (int("".join(num)), count - 1) not in visited:
                dfs(count - 1)
                visited.add((int("".join(num)), count - 1))

            num[i], num[j] = num[j], num[i]

T = int(input())

for test_case in range(1, T + 1):
    num, count = map(int, input().split())
    result = 0
    num = list(str(num))
    visited = set()
    dfs(count)
    print("#" + str(test_case) + " " + str(result))
