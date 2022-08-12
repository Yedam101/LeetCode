class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ['(', ')', '{', '}', '[', ']']
        stack = []
        temp = True

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])

            elif s[i] == ')':
                if not stack:
                    temp = False
                    break
                elif stack[-1] != '(':
                    temp = False
                    break
                elif stack[-1] == '(':
                    stack.pop()
            
            elif s[i] == '}':
                if not stack:
                    temp = False
                    break
                elif stack[-1] != '{':
                    temp = False
                    break
                elif stack[-1] == '{':
                    stack.pop()
                  
            elif s[i] == ']':
                if not stack:
                    temp = False
                    break
                elif stack[-1] != '[':
                    temp = False
                    break
                elif stack[-1] == '[':
                    stack.pop()
         
        if not stack and temp != False:
            return True
        else:
            return False