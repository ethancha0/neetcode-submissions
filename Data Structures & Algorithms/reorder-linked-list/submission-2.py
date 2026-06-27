# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid point 
        left = head 
        right = head 

        while right and right.next:
            left = left.next
            right = right.next.next 

        mid = left 

        # reverse second half 
        prev = None 
        curr = mid 

        while curr:
            temp = curr.next
            curr.next = prev 

            prev = curr
            curr = temp


        # merge
        list1 = head 
        list2 = prev


        while list2: 
            temp1 = list1.next 
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2

        # if odd, set last (end node)  to none 
        if list1:
            list1.next = None



