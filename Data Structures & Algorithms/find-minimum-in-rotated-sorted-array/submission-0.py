class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        min_element=0
        while left<right:
            mini=(left+right)//2
            min_element=min(min_element,nums[mini])
            if nums[mini]>nums[right]:
                left=mini+1
            else:
                right=mini
        return nums[left]
        