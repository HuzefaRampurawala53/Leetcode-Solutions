class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        return nums[k:] + nums[:k]
        