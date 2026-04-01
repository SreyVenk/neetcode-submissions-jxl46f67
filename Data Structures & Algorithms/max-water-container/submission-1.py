class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if area > most:
                most = area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return most