from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    current_weight = 0
    answer = 0
    while truck_weights:
        answer += 1
        a = queue.popleft()
        current_weight -= a
        if current_weight + truck_weights[0] <= weight and len(queue) < bridge_length:
            truck = truck_weights.popleft()
            queue.append(truck)
            current_weight += truck
        elif len(queue) < bridge_length:
            queue.append(0)
    answer += len(queue)
    return answer