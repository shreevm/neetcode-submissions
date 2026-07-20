"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur=head
        while cur:
            new_node=Node(cur.val)
            new_node.next=cur.next
            cur.next=new_node
            cur=new_node.next
        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
        #step3:Sep 
        cur=head
        copy_head=head.next
        copy_cur=copy_head
        while cur:
            cur.next=cur.next.next
            if copy_cur.next:
                copy_cur.next=copy_cur.next.next
            cur=cur.next
            copy_cur=copy_cur.next
        return copy_head
        


        
        