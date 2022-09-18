n = int(input())
component = list(input())
num = []
stack = []
for i in range(n):
    num.append(int(input()))

for i in component:
    if i == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif i == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif i == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(a / b)
    elif i == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(a - b)
    else:
        stack.append(ord(i)-ord("A"))

print(stack[0])