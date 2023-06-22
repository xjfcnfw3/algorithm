import bisect


def solution(info, query):
    condition = {}
    condition[0] = ('cpp', 'java', 'python')
    condition[1] = ('backend', 'frontend')
    condition[2] = ('junior', 'senior')
    condition[3] = ('chicken', 'pizza')

    informations = {}
    informations['cpp'] = {}
    informations['java'] = {}
    informations['python'] = {}

    def make_tree(info, tree):
        for i in info:
            lang, position, level, food, point = i.split()

            if position in tree[lang]:
                if level in tree[lang][position]:
                    if food in tree[lang][position][level]:
                        tree[lang][position][level][food].append(int(point))
                    else:
                        tree[lang][position][level][food] = [int(point)]
                else:
                    tree[lang][position][level] = {}
                    tree[lang][position][level][food] = [int(point)]
            else:
                tree[lang][position] = {}
                tree[lang][position][level] = {}
                tree[lang][position][level][food] = [int(point)]
            tree[lang][position][level][food].sort()

    make_tree(info, informations)

    def make_conditions(q):
        conditions = q.split(" and ")
        food, point = conditions[-1].split(" ")
        conditions[-1] = food
        conditions.append(int(point))
        return conditions

    def search(tree, col, conditions):
        result = 0
        if col == 4:
            index = bisect.bisect_left(tree, conditions[col])
            return len(tree) - index
        if conditions[col] == "-":
            for c in condition[col]:
                if c in tree:
                    result += search(tree[c], col + 1, conditions)
        else:
            if conditions[col] in tree:
                result += search(tree[conditions[col]], col + 1, conditions)
        return result

    answer = []

    for q in query:
        conditions = make_conditions(q)
        answer.append(search(informations, 0, conditions))
    return answer