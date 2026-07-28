# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point (start of second list) 
        slow = head 
        fast = head 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        mid = slow


        #reverse second half
        curr = mid
        prev = None 
        while curr: 
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        #merge 
        list1 = head
        list2 = prev

        while list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1


            list1 = temp1
            list2 = temp2

        #if list1 odd
        if list1: 
            list1.next = None

        

        

        # 2, 4, 6, 8, 10 
        # 10, 8 , 6 



