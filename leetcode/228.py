class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        start = nums[0]
        answer = []
        for i in range(len(nums)):
            if i == len(nums) - 1:
                answer.append(f"{start}->{nums[i]}" if start != nums[i] else f"{start}")
                continue
            if nums[i] + 1 != nums[i + 1]:
                answer.append(f"{start}->{nums[i]}" if start != nums[i] else f"{start}")
                start = nums[i + 1]
        return answer