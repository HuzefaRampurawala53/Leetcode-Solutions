
class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()

        left = 0
        total = 0
        answer = 1

        for right in range(len(nums)):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            answer = max(answer, right - left + 1)

        return answer
