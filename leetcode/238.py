class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] *= nums[i-1] * left[i-1]
        for i in reversed(range(0, len(nums)-1)):
            right[i] *= nums[i+1] * right[i+1]
        result = []
        for i in range(len(nums)):
            result.append(right[i] * left[i])
        return result