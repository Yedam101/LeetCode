class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        def fb(x):
            if x% 15 == 0:
                x = 'FizzBuzz'
            elif x % 3 == 0:
                x = 'Fizz'
            elif x % 5 == 0:
                x = 'Buzz'
            return x    
            
        
        return [str(fb(x)) for x in range(1, n + 1)]
        

                
                
        