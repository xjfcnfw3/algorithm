
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def solution(index, result):
    global answer
    if index == n:
        answer = max(answer, result)
        return
    heart, wight = arr[index]
    if heart <= 0:
        solution(index + 1, result)
    else:
        is_broken = True
        for i in range(n):
            if index == i:
                continue
            if arr[i][0] <= 0:
                continue
            is_broken = False
            temp = result
            arr[i][0] -= wight
            if arr[i][0] <= 0:
                temp += 1
            arr[index][0] -= arr[i][1]
            if arr[index][0] <= 0:
                temp += 1
            solution(index + 1, temp)
            arr[i][0] += wight
            arr[index][0] += arr[i][1]
        if is_broken:
            solution(n, result)


solution(0, 0)
print(answer)
