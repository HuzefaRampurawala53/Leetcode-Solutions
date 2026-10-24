class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        left=0
        right = len(num) - 1
        while right >= 0:
            if int(num[right]) % 2 == 1:
                return num[0:right+1]
            right -= 1
        return ""
        