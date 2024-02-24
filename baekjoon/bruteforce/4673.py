visited = [False] * 100001
def check(num):
    return num + sum(list(map(int, str(num))))

for i in range(1, 10001):
    visited[check(i)] = True
    if not visited[i]:
        print(i)