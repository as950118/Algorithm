class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        nums = nums1 + nums2
        nums.sort()
        if (n+m) % 2:
            return nums[(n+m)//2]
        else:
            return (nums[(n+m)//2] + nums[(n+m)//2 - 1]) / 2