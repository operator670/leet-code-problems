class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = h * width
            max_area = max(area, max_area)
            if height[right] < height[left]:
                right = right - 1
            else:
                left = left + 1
        return max_area