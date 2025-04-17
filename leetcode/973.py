import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        heap = []
        result = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, [dist, point[0], point[1]])

        for _ in range(k):
            data = heapq.heappop(heap)
            result.append(data[1:])

        return result