def solution(cap, n, deliveries, pickups):
    p_end = n - 1
    d_end = n - 1
    answer = 0
    while p_end >= 0 or d_end >= 0:
        while p_end >= 0 and pickups[p_end] == 0:
            p_end -= 1
        while d_end >= 0 and deliveries[d_end] == 0:
            d_end -= 1
        answer += (max(p_end, d_end) + 1) * 2
        p_cap = cap
        d_cap = cap
        while p_end >= 0 and p_cap > 0:
            if pickups[p_end] <= p_cap:
                p_cap -= pickups[p_end]
                pickups[p_end] = 0
                p_end -= 1
            else:
                pickups[p_end] -= p_cap
                p_cap = 0
        while d_end >= 0 and d_cap > 0:
            if deliveries[d_end] <= d_cap:
                d_cap -= deliveries[d_end]
                deliveries[d_end] = 0
                d_end -= 1
            else:
                deliveries[d_end] -= d_cap
                d_cap = 0
    return answer