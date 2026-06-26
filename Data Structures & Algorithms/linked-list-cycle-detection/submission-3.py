# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        left = head 
        right = head

        while left and right: 
            left = left.next

            if right and right.next and right.next.next:
                right = right.next.next
            else:
                return False

            if left == right:
                return True 

        

        return False