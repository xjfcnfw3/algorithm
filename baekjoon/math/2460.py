people = 0
max_num = 0
for i in range(10):
    end, start = map(int, input().split())
    people += start
    people -= end
    if max_num < people:
        max_num = people

print(max_num)