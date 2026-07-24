class Node:

    def __init__(self,key:int,val:int):
        self.key=key
        self.val=val
        self.prev=None
        self.nxt=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.cap=capacity

        #create a dummy node
        self.left,self.right=Node(0,0), Node(0,0)
        self.left.nxt=self.right
        self.right.prev=self.left

    def remove(self,node:Node)-> None:
            prev,nxt=node.prev,node.nxt
            prev.nxt=nxt
            nxt.prev=prev

    def insert(self,node:Node)-> None:
            prev,nxt=self.right.prev,self.right
            prev.nxt=node
            nxt.prev=node
            node.prev=prev
            node.nxt=nxt


        

    def get(self, key: int) -> int:

        if key in self.cache:

            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:


        if key in self.cache:
            self.remove(self.cache[key])

        new_node=Node(key,value)
        self.cache[key]=new_node
        self.insert(new_node)

        if len(self.cache)> self.cap:
            lru=self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

        

