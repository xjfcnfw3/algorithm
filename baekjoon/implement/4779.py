import sys
input = sys.stdin.readline

def cut(start, end):
    s = end - start
    if s == 1:
        return
    for i in range(start + s//3, start + s//3 * 2):
        result[i] = ' '
    cut(start, start + s//3)
    cut(start + s//3 * 2, start + s//3 * 3)

while True:
    try:
        n = int(input())
        result = ['-'] * (3 ** n)
        cut(0, 3 ** n)
        print(''.join(result))
    except:
        break