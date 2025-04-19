class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        def bisect(numbers, target):
            left, right = 0, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] < target:
                    left = mid + 1
                elif numbers[mid] > target:
                    right = mid - 1
                elif numbers[mid] == target:
                    return mid
            return 1e9
        answer = []
        for i in range(len(numbers)):
            result = bisect(numbers[i + 1:], target - numbers[i])
            if result != 1e9:
                answer = [i + 1, i + result + 2]
                break
        return answer