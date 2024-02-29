from collections import deque


def solution(begin, target, words):
    global answer, result

    answer = len(words)
    result = False

    def check(procedure, word):
        num = 0
        for i in range(len(procedure)):
            if procedure[i] != word[i]:
                num += 1
            if num > 1:
                return False
        return True

    def bfs(begin):
        global answer, result
        q = deque()
        q.append([begin, []])

        while q:
            current, path = q.popleft()
            if current == target:
                result = True
                answer = min(answer, len(path))
                continue
            for word in words:
                if check(current, word) and len(path) <= answer:
                    q.append([word, path + [word]])

    bfs(begin)

    if not result:
        return 0

    return answer