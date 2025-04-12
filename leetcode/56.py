from collections import deque
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        q = deque(intervals)
        result = []

        while q:
            current = q.popleft()

            if q:
                if current[1] >= q[0][0]:
                    current = [current[0], max(current[1], q[0][1])]
                    q.popleft()
                    q.appendleft(current)
                    continue
            result.append(current)
        return result