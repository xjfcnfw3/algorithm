n = int(input())

button = set()
result = []


def close_button(command:str, index):
    result.append(command[:index] + "[" + command[index] + "]" + command[index + 1:])


def process1(command:str):
    idx = 0
    for c in command.split():
        if c[0].lower() not in button:
            button.add(c[0].lower())
            close_button(command, idx)
            return True
        idx += len(c) + 1
    return False


def process2(command: str):
    for i in range(len(command)):
        if command[i] != " " and command[i].lower() not in button:
            button.add(command[i].lower())
            close_button(command, i)
            return True
    return False


for _ in range(n):
    command = input()
    if process1(command):
        continue
    if process2(command):
        continue
    result.append(command)
print(*result, sep='\n')
