while True:
    try:
        arr = list(input())
        char = [0, 0, 0, 0]
        for i in arr:
            if ord('Z') >= ord(i) >= ord('A'):
                char[1] += 1
            elif ord('z') >= ord(i) >= ord('a'):
                char[0] += 1
            elif ord('9') >= ord(i) >= ord('0'):
                char[2] += 1
            elif i == " ":
                char[3] += 1
        print(*char)
    except EOFError:
        break