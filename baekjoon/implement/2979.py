cost = list(map(int, input().split()))
arr = []
max_time = 0
current_num = 0
result = 0
for i in range(3):
    start, end = map(int, input().split())
    arr.append([start, end])
    if max_time < end:
        max_time = end

for i in range(1, max_time+1):
    for j in arr:
        if i == j[0]:
            current_num += 1
        elif i == j[1]:
            current_num -= 1
    if current_num>0:
        result += current_num*cost[current_num-1]

print(result)