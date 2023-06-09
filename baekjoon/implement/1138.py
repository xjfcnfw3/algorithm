

n = int(input())
q = []
arr = list(map(int, input().split()))
index_list = [i for i in range(n)]
result = [0] * n


for i in range(1, n + 1):
    result[index_list[arr[i - 1]]] = i
    del index_list[arr[i - 1]]

print(" ".join(map(str, result)))