class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur = sum(nums[0:k])
        ret = cur
        for i in range(1, n-k+1):
            cur = cur - nums[i-1] + nums[i+k-1]
            ret = max(ret, cur)
        return ret/k