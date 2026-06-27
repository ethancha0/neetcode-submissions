# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0 

        count = head
        while count: 
            count = count.next
            length +=1 
        
        
        remove = length - n 

        if remove < 0:
            return None
        elif remove == 0:
            return head.next

        curr = head 
        anchor = curr
        tracker = 0 

        while curr and tracker < remove-1:
            curr = curr.next
            tracker +=1
        

        curr.next = curr.next.next
            

        return anchor
