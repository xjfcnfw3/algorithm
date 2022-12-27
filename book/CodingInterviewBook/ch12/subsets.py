class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(elements, start: int):
            result.append(elements)

            for i in range(start, len(nums)):
                dfs(elements + [nums[i]], i + 1)

        dfs([], 0)
        return result