n = int(input())
arr = input().split()
min_result = "99999999999999"
max_result = str(0)
def dfs(result):
    global min_result, max_result
    if len(result) == len(arr) + 1:
        num = "".join(list(map(str, result)))
        if int(num) < int(min_result):
            min_result = num
        if int(num) > int(max_result):
            max_result = num
        return

    if arr[len(result) - 1] == "<":
        for num in range(result[-1] + 1, 10):
            if num not in result:
                dfs(result + [num])
    else:
        for num in range(0, result[-1]):
            if num not in result:
                dfs(result + [num])

for i in range(0, 10):
    dfs([i])

print(max_result)
print(min_result)