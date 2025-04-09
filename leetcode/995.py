class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        answer = 0
        flipped = 0
        isFlipped = [0] * len(nums)
        for i in range(len(nums)):
            if i >= k:
                flipped ^= isFlipped[i - k]
            if flipped == nums[i]:
                if i + k > len(nums):
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                answer += 1
        return answer