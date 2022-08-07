class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            idx = 0
            for i in range(len(nums) +1):

                if i == len(nums): 
                    
                    return idx
                elif target < nums[i]:
                    return idx
                elif target > nums[i]:
                    idx += 1
                   