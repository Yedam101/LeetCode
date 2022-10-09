class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if 0 not in nums:
            ans = []
            mul = [nums[0]] +[0]*(len(nums)-1)
            for i in range(1, len(nums)):
                mul[i] = mul[i-1]*nums[i]

            for j in range(len(nums)):
                ans.append(int(mul[-1]/nums[j]))
            return ans
        
        else:
            ans = [0]*len(nums)
            zero = nums.index(0)
            nums.remove(0)
            mul = [nums[0]]
            for i in range(1, len(nums)):
                mul.append(mul[i-1]*nums[i])
            
            ans[zero] = mul[-1]
            
            return ans
            
            

        
        
            
        
        
        