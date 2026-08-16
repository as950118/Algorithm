from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
        # n = len(nums)
        # dp = [1] * n
        # for i in range(n - 2, -1, -1):
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)