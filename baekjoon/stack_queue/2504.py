arr = list(input())
stack = []
score = 0

for i in arr:
    if i == '(' or i == '[':
        stack.append(i)
    if i == ')' or i == ']':
        if stack is None:
            print(0)
            exit()
        else:
            d = stack.pop(-1)
            if d == '(':
                if i == ')':

