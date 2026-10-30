class Solution:
    def frequencySort(self, s: str) -> str:
        
        hashmaps = {}

        for characters in s:
            hashmaps[characters] = hashmaps.get(characters, 0) + 1

        sorted_char = sorted(
            hashmaps.items(),
            key=lambda x: (-x[1], x[0])
        )

        result = ""

        for characters, freq in sorted_char:
            result += characters*freq

        return result
        