class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = len(height)-1
        area = 0

        while l < r:
            area = max(area, (r-l)*(min(height[r],height[l])))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return area