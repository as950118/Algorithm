class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        exists_zero = 0 in nums
        all_zero = sum([num!=0 for num in nums]) == 0
        one_zero = sum([num!=0 for num in nums]) == 1
        more_zero = not all_zero and sum([num==0 for num in nums]) > 1
        n = len(nums)
        for num in nums:
            if num != 0:
                prod *= num
        ret = []
        for num in nums:
            if num != 0:
                if exists_zero or (one_zero and not n==2):
                    ret.append(0)
                else:
                    ret.append(prod//num)
            else:
                if all_zero or (one_zero and not n==2) or more_zero:
                    ret.append(0)
                else:
                    ret.append(prod)
        return ret