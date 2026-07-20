from collections import defaultdict
from typing import List 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = defaultdict(int)
        for num in nums:
                seen[num]+=1 
        sorted_list=sorted(seen.items(),key=lambda x:x[1], reverse=True)
        topk=[items[0] for items in sorted_list[:k]]
        return topk
