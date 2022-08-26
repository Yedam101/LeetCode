class Solution:
    def isPalindrome(self, s: str) -> bool:

        if [x for x in s.lower() if x.isalnum()] == [x for x in s.lower() if x.isalnum()][::-1]:
            return True
        else:
            return False