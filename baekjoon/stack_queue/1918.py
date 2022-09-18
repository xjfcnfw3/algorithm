arr = list(input())
result = []
stack = []
num = 0
for i in arr:
    if i == "*" and i =="+" and i == "-" and i == "/":
        stack.append(i)
    elif i == "(":
        num += 1
    elif i == ")":
        num -= 1
        if num == 0:
            while stack:
                result.append(stack.pop())
    else:
        result.append(i)

while stack:
    result.append(stack.pop())
print(result)