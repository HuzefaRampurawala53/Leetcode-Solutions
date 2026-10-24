class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for i in s:
            i = i.lower()

            if i.isalnum():
                cleaned = cleaned + i
                
        n = len(cleaned)
        left = 0
        right = n - 1
        while left < right:
            if cleaned[left] == cleaned[right]:
                left = left + 1
                right = right - 1
            else:
                return False
                
        return True
        