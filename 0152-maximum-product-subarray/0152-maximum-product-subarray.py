class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max_prd = min_prd = nums[0]
        for num in nums[1:]:
            candidates = (num, max_prd * num, min_prd * num)
            max_prd = max(candidates)
            min_prd = min(candidates)
            result = max(result, max_prd)
        return result