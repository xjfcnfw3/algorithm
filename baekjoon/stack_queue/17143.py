revers = True
c = input()
stack = []
result = []
for i in c:
    if i == "<":
        revers = False
        while len(stack):
            result.append(stack.pop())
        result.append("<")
    elif i == ">":
        revers = True
        result.append(">")
    elif i == " ":
        while len(stack):
            result.append(stack.pop())
        result.append(" ")
    else:
        if revers:
            stack.append(i)
        else:
            result.append(i)
while len(stack):
    result.append(stack.pop())
print("".join(result))