from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s)==sorted(t)

        # if len(s)!=len(t):
        #     return False

        # # for i in len(s):
        # #     arr[i] = s[i]

        # # for i in len(t):
        # #     if t[i]

        # for i in range(len(t)):
        #     if t[i] in s:
        #         s=s.replace(t[i],"")

        # return len(s)==0
        