def check(w):
    stack = []
    num_open = 0
    num_close = 0
    offset = True
    for i in w:
        if i == "(":
            num_open += 1
            stack.append(1)
        elif i == ")":
            num_close += 1
            if stack:
                stack.pop()
            else:
                offset = False
    if offset and not stack:
        return 2
    elif num_open == num_close:
        return 1
    return 0

def step(w):
    if not w:
        return w
    num_open = 0
    num_close = 0
    index = 0
    for i in range(len(w)):
        if w[i] == "(":
            num_open += 1
        elif w[i] == ")":
            num_close += 1
        if num_open == num_close:
            index = i
            break
    u, v = w[:index + 1], w[index + 1:]
    if check(u) == 2:
        return u + step(v)
    else:
        return "(" + step(v) + ")" + reverse_step(u[1:-1])
def reverse_step(w):
    result = ''
    for i in w:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(p):
    if check(p) == 2:
        return p
    return step(p)