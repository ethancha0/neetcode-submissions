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
        
        myMap = {None:None}

        curr = head
        while curr: 
            myMap[curr] = Node(curr.val)
            curr = curr.next


        curr = head 
        while curr:
            myMap[curr].next = myMap[curr.next]
            myMap[curr].random = myMap[curr.random]

            curr = curr.next

        return myMap[head]
