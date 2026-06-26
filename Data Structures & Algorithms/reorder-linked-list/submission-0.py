# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. find midpoint 
        left = head 
        right = head

        while right and right.next:
            left = left.next
            right = right.next.next
        
        mid = left 

        # 2. reverse second half 
        prev = None 
        curr = mid 

        while curr: 
            temp = curr.next
            curr.next = prev 

            prev = curr
            curr = temp 


        # 3. merge back 
        first = head 
        second = prev

        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        

        
        

            
