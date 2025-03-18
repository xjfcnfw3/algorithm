from itertools import combinations


def solution(relation):
    answer = []
    columns = [i for i in range(len(relation[0]))]

    def check(key):
        for a in answer:
            temp = True
            for c in a:
                if c not in key:
                    temp = False
                    break
            if temp:
                return False
        return True

    for i in range(1, len(relation[0]) + 1):
        for r in combinations(columns, i):
            tup = set()
            for row in relation:
                temp = ""
                for col in r:
                    temp += str(row[col]) + " " + str(col) + " "
                tup.add(temp)
            if len(tup) == len(relation):
                if check(r):
                    answer.append(r)

    return len(answer)