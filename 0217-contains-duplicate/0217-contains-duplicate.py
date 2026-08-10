class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False