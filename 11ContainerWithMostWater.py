class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(height) - 1
        while l < r:
            water = min(height[l], height[r]) * (r - l)
            maxWater = max(maxWater, water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater