class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

            for i in range(len(digits)):
                digits[i] = str(digits[i])

            dig = int(''.join(digits)) + 1

            dig_n = list(str(dig))
            return dig_n


            
            
        