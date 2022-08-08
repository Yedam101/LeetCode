class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse = True)
        count = 0
        l = int(len(piles)/3)

        for i in range(l):
            count += piles[i*2+1]
        
        return count
        