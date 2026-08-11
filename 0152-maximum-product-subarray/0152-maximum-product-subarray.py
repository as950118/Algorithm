class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prd = nums[0]
        neg_max_prd = nums[0]
        cur = max_prd
        neg_cur = neg_max_prd
        for num in nums[1:]:
            cur, neg_cur = max(num, cur*num, neg_cur*num), min(num, cur*num, neg_cur*num)
            # cur = max(num, cur*num, neg_cur*num)
            # neg_cur = min(num, cur*num, neg_cur*num)
            max_prd = max(max_prd, cur)
            neg_max_prd = min(neg_max_prd, cur)
            print(max_prd, neg_max_prd)
        return max(max_prd, neg_max_prd)