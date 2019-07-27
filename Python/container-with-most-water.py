class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        most_water = 0
        left = 0
        right = len(height)-1
        
        while (left < right):
            area = (right - left)* min(height[left], height[right])
            if area > most_water:
                most_water = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most_water
