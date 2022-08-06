class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i = 0
        s = sum(nums[:3])

        if len(nums) > 3:
            for i in range(len(nums)-2):
                j, k = i+1, len(nums)-1

                while j < k:
                    if abs(target-s) < abs(target - (nums[i] + nums[j] + nums[k])):
                        s = s
                    else:
                        s = nums[i] + nums[j] + nums[k]

                    if target > (nums[i] + nums[j] + nums[k]):
                        j += 1

                    else:
                        k -= 1

            return s


        else:
             return sum(nums)