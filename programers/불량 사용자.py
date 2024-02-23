def check(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(banned_id)):
        if banned_id[i] == "*":
            continue
        if banned_id[i] != user_id[i]:
            return False
    return True

def dfs(s, depth, banned_id, user_id, visited):
    global result
    if depth == len(banned_id):
        result.add("".join(sorted(list(map(str, s)))))
        return
    for i in range(len(user_id)):
        if not visited[i] and check(user_id[i], banned_id[depth]):
            visited[i] = True
            dfs(s + [i], depth + 1, banned_id, user_id, visited)
            visited[i] = False
def solution(user_id, banned_id):
    global result
    result = set()
    visited = [False] * len(user_id)
    dfs([], 0, banned_id, user_id, visited)
    return len(result)