def solution(name):
    min_move = len(name) - 1
    spell_move = 0

    for i, c in enumerate(name):
        spell_move += min(ord("Z") - ord(c) + 1, ord(c) - ord("A"))

        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        min_move = min(min_move, i * 2 + len(name) - next, i + (len(name) - next) * 2)

    return min_move + spell_move