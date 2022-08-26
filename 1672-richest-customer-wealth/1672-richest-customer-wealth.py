class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        count, i = 0, 0
        
        while i < len(accounts):
            count =  max(count, sum(accounts[i]))
            i += 1             
        
        return count