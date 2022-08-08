class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [i for i in str(num)]
        nums.sort()


        dbsum = [int(nums[0]+nums[3]), int(nums[1]+nums[2])]

        return sum(dbsum)