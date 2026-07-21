class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        res=[1]*len(nums)
        # calculate the left product of the number 
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i] #multiply by the previous number and store the previous number pro in the prefix
        
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res