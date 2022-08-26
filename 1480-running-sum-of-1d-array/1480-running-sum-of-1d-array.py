class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        

        
        return [sum(nums[:i])+nums[i] if i >=1 else nums[i] for i in range(len(nums))]
 

    
      
