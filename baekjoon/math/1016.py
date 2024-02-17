min_, max_ = map(int, input().split())
visited = [False] * (max_ - min_ + 1)
result = 0
def check():
    global result
    for current in range(2, int(max_**(1/2)) + 1):
        m = current ** 2
        number = (min_ // m) * (current ** 2)
        while number <= max_:
            if min_ <= number <= max_:
                if not visited[number - min_]:
                    result += 1
                visited[number - min_] = True
            number += m
check()
print(len(visited) - result)