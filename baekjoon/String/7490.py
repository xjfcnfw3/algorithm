t = int(input())

def check(result, n):
    s = ""
    for i in range(1, n + 1):
        s += str(i)
        if i == n:
            continue
        s += result[i - 1]

    op = s.replace(" ", "")
    num = 0
    temp = ""
    operation = "+"
    for c in op:
        if c == "+" or c == "-":
            if operation == "+":
                num += int(temp)
            else:
                num -= int(temp)
            temp = ""
            operation = c
        else:
            temp += c
    if operation == "+":
        num += int(temp)
    else:
        num -= int(temp)
    if num == 0:
        print(s)


def dfs(result, n):
    if len(result) == n - 1:
        check(result, n)
        return

    dfs(result + [" "], n)
    dfs(result + ["+"], n)
    dfs(result + ["-"], n)


for i in range(t):
    n = int(input())
    dfs([], n)
    print()

