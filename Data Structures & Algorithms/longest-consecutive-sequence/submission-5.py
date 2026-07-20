class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        longest=0
        seen=set(nums)

        for i in  nums:
            if (i-1) not in seen:
                length=0
                while (i+length) in seen:
                    length+=1
                longest=max(length,longest)
        return longest 
                
        
