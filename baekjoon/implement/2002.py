from collections import deque
n = int(input())

in_cars = deque()
out_cars = deque()
result = []
for _ in range(n):
    in_cars.append(input())

for _ in range(n):
    out_cars.append(input())

while in_cars:
    current = in_cars.popleft()

    if current in result:
        continue

    if not out_cars:
        continue

    if out_cars[0] == current:
        out_cars.popleft()
    else:
        while out_cars and out_cars[0] != current:
            car = out_cars.popleft()
            result.append(car)
        if out_cars:
            out_cars.popleft()

print(len(result))