class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(elements, start: int, value: int):
            if value >= target:
                if value == target:
                    result.append(elements[:])
                    return
                else:
                    return

            for i in range(start, len(candidates)):
                elements.append(candidates[i])
                dfs(elements, i, value + candidates[i])
                elements.pop()

        dfs([], 0, 0)
        return result