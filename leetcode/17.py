class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        def dfs(depth, numbers):
            if depth == len(digits):
                result.append(numbers)
                return
            for i in dic[digits[depth]]:
                dfs(depth + 1, numbers + i)
        dic = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno",
        "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        result = []
        dfs(0, "")
        return result