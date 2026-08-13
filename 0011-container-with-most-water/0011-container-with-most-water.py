class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l<r:
            left = height[l]
            right = height[r]
            area = (r-l) * min(left, right)
            max_area = max(max_area, area)
            if left < right:
                l += 1
            else:
                r -= 1
        return max_area
        # height_to_idx = {h:[] for h in height}
        # for i, h in enumerate(height):
        #     height_to_idx[h].append(i)
        # unique_height = list(height_to_idx.keys())
        # unique_height.sort()
        # # for i in range(len(unique_height)-1, -1, -1):
            