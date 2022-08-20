class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = [2**x for x in range(32)]


        if n in a:
            return True
        else:
            return False
        