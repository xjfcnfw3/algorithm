import sys

input = sys.stdin.readline

def exec(commands, num):
    stk = [num]
    for command in commands:
        if command[0:3] == "NUM":
            c, n = command.split(" ")
            stk.append(int(n))
        elif command == "POP":
            if not stk:
                return "ERROR"
            stk.pop()
        elif command == "INV":
            stk[-1] *= -1
        elif command == "DUP":
            stk.append(stk[-1])
        elif command == "SWP":
            if len(stk) < 2:
                return "ERROR"
            stk[-1], stk[-2] = stk[-2], stk[-1]
        elif command == "ADD":
            if len(stk) < 2:
                return "ERROR"
            num = stk.pop()
            if abs(stk[-1] + num) > 1e9:
                return "ERROR"
            stk[-1] += num
        elif command == "MUL":
            if len(stk) < 2:
                return "ERROR"
            num = stk.pop()
            if abs(stk[-1] * num) > 1e9:
                return "ERROR"
            stk[-1] *= num
        elif command == "SUB":
            if len(stk) < 2:
                return "ERROR"
            num = stk.pop()
            if abs(stk[-1] - num) > 1e9:
                return "ERROR"
            stk[-1] -= num
        elif command == "DIV":
            if len(stk) < 2:
                return "ERROR"
            a, b = stk.pop(), stk.pop()
            if a == 0:
                return "ERROR"
            temp = abs(b) // abs(a)
            if (a > 0 > b) or (a < 0 < b):
                temp = -temp
            if abs(temp) > 10 ** 9:
                return "ERROR"
            stk.append(temp)
        elif command == "MOD":
            if len(stk) < 2:
                return "ERROR"
            a, b = stk.pop(), stk.pop()
            if a == 0:
                return "ERROR"
            temp = abs(b) % abs(a)
            if b < 0:
                temp = -temp
            if abs(temp) > 10 ** 9:
                return "ERROR"
            stk.append(temp)
        else:
            return "ERROR"
    if len(stk) == 1:
        return stk[0]
    return "ERROR"

while True:
    commands = []
    while True:
        command = input().strip()
        if command == "QUIT":
            quit()
        if command == "END":
            break
        commands.append(command)
    n = int(input())
    for _ in range(n):
        num = int(input())
        print(exec(commands, num))
    print()
    input()
