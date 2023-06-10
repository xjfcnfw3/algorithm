from collections import defaultdict

n = int(input())
m = int(input())

arr = list(map(int, input().split()))

photo = 0

photo_line = defaultdict(list)

photos = {}


def insert_photo(num, index):
    photo_line[1].append(num)
    photos[num] = [1, index]


def move_photo(num):
    count = photos[num][0]
    photo_line[count].remove(num)
    photo_line[count + 1].append(num)
    photos[num][0] += 1


def remove_photo():
    for i in range(1, m + 1):
        if photo_line[i]:
            deleted = -1
            min_count = 99999
            for num in photo_line[i]:
                if photos[num][1] < min_count:
                    min_count = photos[num][1]
                    deleted = num
            photos.pop(deleted)
            photo_line[i].remove(deleted)
            break


for i in range(len(arr)):
    if arr[i] in photos:
        move_photo(arr[i])
    else:
        if photo < n:
            insert_photo(arr[i], i)
            photo += 1
        else:
            remove_photo()
            insert_photo(arr[i], i)

print(" ".join(list(map(str, sorted(photos.keys())))))
