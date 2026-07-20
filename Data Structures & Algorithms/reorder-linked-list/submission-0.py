# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        #find the middle value 
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        #rev the second half
        curr,prev=slow.next,None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        slow.next=None
        # merge the two halves

        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
            