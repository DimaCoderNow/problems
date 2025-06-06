class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if (r - l) * min(height[r], height[l]) > res:
                res =  (r - l) * min(height[r], height[l])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
