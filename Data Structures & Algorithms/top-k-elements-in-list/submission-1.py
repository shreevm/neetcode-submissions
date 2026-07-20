class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={} # count the freq
        for n in nums:
            count[n]=1+count.get(n,0) # maps element to the freq
        # this is to get the top k element 
        return heapq.nlargest(k, count.keys(), key=count.get)
