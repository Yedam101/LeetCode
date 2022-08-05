class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}
        
        for i, num in enumerate(nums):
            hash[num] = i
            
        pairs = [target - x for x in nums]
        
        for i, pair in enumerate(pairs):
            if pair in hash and hash[pair] != i:
                return [i, hash[pair]]
            