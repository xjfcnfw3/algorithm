a = input()
b = input()

result = False


def dfs(value):
    global result, a
    if value == a:
        print(1)
        exit(0)
    if len(value) == 0:
        return
    if value[-1] == 'A':
        dfs(value[:-1])
    if value[0] == 'B':
        dfs(value[1:][::-1])


dfs(b)

print('0')
