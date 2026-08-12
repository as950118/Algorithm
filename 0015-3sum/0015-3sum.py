class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []
        n = len(nums)
        nums.sort()
        lo = 0
        mid = lo+1
        hi = n-1
        while True:
            if mid >= hi:
                lo += 1
                mid = lo+1
                hi = n-1
            if lo > n-3 or nums[lo] > 0:
                break
            if lo > 0 and nums[lo] == nums[lo - 1]:
                lo += 1
                mid = lo+1
                hi = n-1
                continue
            cur = nums[lo] + nums[mid] + nums[hi]
            if cur == 0:
                ret.append([nums[lo], nums[mid], nums[hi]])
                mid += 1
                hi -= 1
                while mid < hi and nums[mid] == nums[mid - 1]:
                    mid += 1
                while mid < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1

            if cur < 0:
                mid += 1
            elif cur > 0:
                hi -= 1

            

        return ret