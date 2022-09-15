import sys
left = list(input())
right = []

n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if len(left) != 0:
            right.append(left.pop())
    elif command[0] == 'D':
        if len(right) != 0:
            left.append(right.pop())
    elif command[0] == 'B':
        if len(left) != 0:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print("".join(left+list(reversed(right))))