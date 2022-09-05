class Solution:
    def dfs(self, Digits, sequences):
        if len(sequences) == self.lenchar:
            self.answer.append("".join(sequences))
        
        if Digits:
            newseq = Digits.pop(0)
            newchars = self.Dict[newseq]
            for char in newchars:
                self.dfs(Digits[:], sequences + [char])
                
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        Digits = list(digits)
        self.answer = []
        self.lenchar = len(Digits)


        self.Dict = {'2': ['a','b','c'], '3': ['d','e','f'], 
                     '4':['g','h','i'], '5':['j','k','l'],
                     '6':['m','n','o'], '7':['p','q','r','s'],
                     '8':['t','u','v'], '9':['w','x','y','z']}
        
        self.dfs(Digits[:], [])
        
        return self.answer

        
        