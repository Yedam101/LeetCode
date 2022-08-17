class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        real = [i for i in range(len(nums)+1)]
        a = list(set(real)-set(nums))
        return a.pop()
        