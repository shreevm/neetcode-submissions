import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        seen={}
        max_no=0
        cur_sum=0
        for i in piles:
          cur_sum+=i
          max_no=max(max_no,i)
        
        low, high = 1, max_no
        res = max_no
        while low <= high:
            k = (low + high) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        return res