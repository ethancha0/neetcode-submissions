# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # section 1: find midpoint 
        left = head 
        right = head 
        while right and right.next:
            left = left.next
            right = right.next.next

        mid = left 

        # section 2: reverse list 
        prev = None 
        
        while mid: 
            temp = mid.next
            mid.next = prev

            prev = mid 
            mid = temp 

        # section 3: join lists 
        list1 = head
        list2 = prev 

        while list2: 
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2 

        # we must set the last node to None to finalize the list 
        # if we had an odd length like [1, 2, 3] and [4, 5]
        # 3 could point to someting random so we need to end it 
        if list1:
            list1.next = None
        



