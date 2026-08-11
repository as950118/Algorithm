class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_nums = nums[0]
        cur = max_nums
        for num in nums[1:]:
            cur = max(num, cur+num)
            max_nums = max(max_nums, cur)
        return max_nums

        