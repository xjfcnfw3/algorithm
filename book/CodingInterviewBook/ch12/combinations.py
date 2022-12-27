class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                result.append(elements[:])
                return

            for e in range(start, n + 1):
                elements.append(e)
                dfs(elements, e + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result