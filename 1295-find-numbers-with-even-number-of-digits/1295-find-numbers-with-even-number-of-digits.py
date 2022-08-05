class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 리스트컴프리헨션으로 풀어보기
        
        result = [str(i) for i in nums]
        res = [i for i in result if len(i)%2 ==0]
        
        return len(res)