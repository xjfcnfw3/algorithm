n = int(input())
arr = [input() for _ in range(n)]
result = n
for word in arr:
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            continue
        elif word[i] in word[i + 1:]:
            result -= 1
            break
print(result)