class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stones = Counter(stones)
        count = 0
        
        for i in range(len(jewels)):
            if jewels[i] in stones.keys():
                count += stones[jewels[i]]
        
        return count
    
    
