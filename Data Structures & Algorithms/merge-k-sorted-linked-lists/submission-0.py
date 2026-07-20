# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush,heappop
from itertools import count
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
         dummy=ListNode(0)
         curr=dummy
         heap=[]
         Counter=count()

         for l in lists:
            if l:
                heappush(heap,(l.val,next(Counter),l))

         while heap:
            val,_,node=heappop(heap)
            curr.next=node
            curr=curr.next
            if node.next:
                heappush(heap,(node.next.val,next(Counter),node.next))

         return dummy.next
