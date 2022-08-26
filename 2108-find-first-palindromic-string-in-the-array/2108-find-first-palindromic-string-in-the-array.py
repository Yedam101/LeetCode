class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                return words[i]
                break
            elif i == len(words)-1:
                return ""
        

            
        