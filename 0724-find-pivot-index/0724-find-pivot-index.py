class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        half_nums = sum_nums//2
        cur = 0
        for i, num in enumerate(nums):
            if cur == (sum_nums-num)/2:
                return i
            cur += num
        return -1
