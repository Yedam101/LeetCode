class Solution:
    def maxArea(self, height: List[int]) -> int:
        
            left = 0 
            right = len(height) -1

            area = 0

            while left < right:
                area = max(area, (right-left)*(min(height[right],height[left])))
                if height[right] >= height[left]:
                    left += 1
                elif height[right] < height[left]:
                    right -= 1

            return area
        