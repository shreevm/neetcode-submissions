class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        seen={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack=[]



        for i in range(n):
            if s[i] in seen.keys() and not stack:
                return False  
            elif s[i] in seen.values():
                stack.append(s[i])
            elif s[i] in seen.keys() and stack[-1]==seen[s[i]]:
                stack.pop()
            else:
                return False

        
        return len(stack)==0