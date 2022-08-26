class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ran = list(ransomNote)
        mag = list(magazine)
        
        while ran:
            if ran[0] not in mag:
                return False
                break
            else:
                mag.remove(ran[0])
                ran.pop(0)

        if not ran:
            return True

        
