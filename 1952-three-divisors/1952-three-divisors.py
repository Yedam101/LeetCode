class Solution:
    def isThree(self, n: int) -> bool:
        
            import math
            if n > 1:
                m = math.sqrt(n)
                
                if m.is_integer() == 1:
                    pass
                else:
                    return False



                for i in range(2, int(math.sqrt(m)) + 1):
                    if m % i == 0:
                        return False

                if m*m == n:
                    return True
            else:
                return False
        