
start = input().rstrip()
arr = list(start)

stk = []
pair = []
result = []

for i in range(len(arr)):
    if arr[i] == "(":
        stk.append(i)
    elif arr[i] == ")":
        pair.append((stk.pop(), i))

def dfs(r, index):
    global start
    if index >= len(pair):
        current = arr.copy()
        for x, y in r:
            current[x] = ""
            current[y] = ""
        str = "".join(current)
        if str not in result and str != start:
            result.append(str)
        return
    dfs(r, index + 1)
    dfs(r + [pair[index]], index + 1)

dfs([], 0)
dfs([pair[0]], 0)

result.sort()
print(*result, sep='\n')