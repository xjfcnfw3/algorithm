def dfs(tree, parent):
    mid = len(tree) // 2
    if tree:
        son = (tree[mid] == "1")
    else:
        return True

    if son and not parent:
        return False
    return dfs(tree[:mid], son) and dfs(tree[mid + 1:], son)


def check(num):
    if num == 1:
        return True
    b = list(bin(num)[2:])
    depth = 1
    temp = 1
    while temp < len(b):
        temp += 2 ** depth
        depth += 1
    b = [0] * (temp - len(b)) + b
    return b[len(b) // 2] == "1" and dfs(b, True)


def solution(numbers):
    answer = []
    for num in numbers:
        if check(num):
            answer.append(1)
        else:
            answer.append(0)
    return answer