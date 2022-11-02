class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr =[]
        for c in s:
            if(c.isalnum()):
                arr.append(c.lower())
        arr = list(reversed(arr))
        while len(arr) > 1:
            if arr.pop() != arr.pop(0) :
                return False
        return True