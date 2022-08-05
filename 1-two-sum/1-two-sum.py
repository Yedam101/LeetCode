class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = [target - x for x in nums]
        
        for i, pair in enumerate(pairs):
            if pair in nums and i != nums.index(pair):
                return [i, nums.index(pair)]
        
