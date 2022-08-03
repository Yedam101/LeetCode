class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if 0 < i // 10 < 10:
                count += 1
            elif 0 < i // 1000 < 10:
                count += 1
            elif 0 < i // 100000 < 10:
                count += 1 

        return count
        