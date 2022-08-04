class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        num = Counter(nums)

        x = {k:v for k, v in num.items() if v != 1}
        y = list(x.values())
        y

        count = 0

        for i in range(len(y)):
            y[i] = (y[i]*(y[i]-1))/2
            count += y[i]

        return int(count)
        