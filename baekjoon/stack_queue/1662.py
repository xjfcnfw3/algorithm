s = input()
stk = []
temp = ""
result = 0
for c in s:
    if c == '(':
        stk.append([result - 1, temp])
        result = 0
    elif c == ")":
        c = stk.pop()
        result = c[0] + result * int(c[1])
    else:
        result += 1
        temp = int(c)

print(result)