class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

                i = 0

                while i < len(words):
                    if words[i] == words[i][::-1]:
                        return words[i]
                        break
                        
                    else:
                        i += 1
                        if i == len(words):
                            return ""

        