def solution(n):
    global answer
    answer = 0

    arr = [0] * n

    def check(x):
        for i in range(x):
            if arr[i] == arr[x] or x - i == abs(arr[i] - arr[x]):
                return False
        return True

    def dfs(depth):
        global answer
        if depth == n:
            answer += 1
            return
        for i in range(n):
            arr[depth] = i
            if check(depth):
                dfs(depth + 1)

    dfs(0)
    return answer