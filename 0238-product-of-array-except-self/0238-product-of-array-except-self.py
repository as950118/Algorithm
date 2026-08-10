class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = 1
        n = len(nums)
        for i in range(n):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res