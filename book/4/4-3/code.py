position = input()
x = int(ord(position[0]))- int(ord('a')) + 1
y = int(position[1])
moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]
result = 0
for move in moves:
    if x+move[0] >= 1 and x + move[0] <=8 and y+move[1] >= 1 and y + move[1] <=8:
        result += 1

print(result)