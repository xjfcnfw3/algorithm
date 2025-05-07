class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(elements, start: int):
            if len(elements) > len(nums):
                return
            result.append(elements[:])

            for i in range(start, len(nums)):
                elements.append(nums[i])
                dfs(elements, i + 1)
                elements.pop()

        dfs([], 0)
        return result