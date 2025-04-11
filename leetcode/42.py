class Solution:
    def trap(self, height: list[int]) -> int:
        if  not height:
            return 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        volume = 0

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left +=1
            else:
                volume += right_max - height[right]
                right -=1
        return volume