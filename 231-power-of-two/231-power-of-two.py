class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        elif n%2 == 1 or n ==0:
            return False

        return Solution().isPowerOfTwo(n/2)
        