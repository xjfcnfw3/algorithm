n, m = map(int, input().split())
x, y, direction = map(int, input().split())
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
map = []
for i in range(n):
    row = map(int, input().split())
    map.append(row)

result = 0
can_move = True
while(can_move):
    x += moves[direction][0]
    y += moves[direction][1]




