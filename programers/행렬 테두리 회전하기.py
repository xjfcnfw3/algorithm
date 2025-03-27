def solution(rows, columns, queries):
    answer = []
    m = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            m[row][col] = t
            t += 1

    def get_positions(query):
        x1, y1, x2, y2 = query
        return [x1 - 1, y1 - 1, x2 - 1, y2 - 1]

    def move(query):
        x1, y1, x2, y2 = get_positions(query)
        result = m[x1][y1]
        temp = m[x1][y1]

        for x in range(x1, x2):
            num = m[x + 1][y1]
            m[x][y1] = num
            result = min(num, result)
        for y in range(y1, y2):
            num = m[x2][y + 1]
            m[x2][y] = num
            result = min(num, result)
        for x in range(x2, x1, -1):
            num = m[x - 1][y2]
            m[x][y2] = num
            result = min(num, result)
        for y in range(y2, y1, -1):
            num = m[x1][y - 1]
            m[x1][y] = num
            result = min(num, result)
        m[x1][y1 + 1] = temp

        return result

    for query in queries:
        answer.append(move(query))
    return answer