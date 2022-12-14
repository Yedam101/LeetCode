class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = set()
        
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple([nums[i], nums[j], nums[k]]))
                    j, k = j+1, k-1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
                    
        return list(result)
                    
        