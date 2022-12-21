class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(start: int, end: int) -> str:
            while start >= 0 and end <= len(s) and s[start] == s[end - 1]:
                start -= 1
                end += 1
            return s[start + 1:end - 1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result
