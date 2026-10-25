class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        left = 0 
        while left < len(strs[0]):
            for word in strs[1: ]:
                if left>=len(word) or strs[0][left] != word[left]:
                    return strs[0][:left]
            left = left + 1

        return strs[0]
        