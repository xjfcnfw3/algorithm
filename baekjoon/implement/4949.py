while True:
    bal = 1
    stack = []
    s = input()
    if s == ".":
        exit()
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if stack:
                t = stack.pop(-1)
                if t == '(' and i == ']':
                    bal = 0
                    break
                if t == '[' and i == ')':
                    bal = 0
                    break
            else:
                bal = 0
                break
    if bal == 0 or stack:
        print("no")
    elif bal == 1:
        print("yes")
