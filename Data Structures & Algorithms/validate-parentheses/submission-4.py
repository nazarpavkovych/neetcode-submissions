class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mnozina = {'(', '{','['}
        for i in s:
            if i in mnozina:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack[-1]=='(':
                    stack.pop()
                
                elif i ==']' and stack[-1] == '[':
                    stack.pop()
                elif i =='}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack)==0
