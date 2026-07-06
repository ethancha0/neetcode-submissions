# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0 
        dummy = ListNode() 
        curr = dummy 

        while l1 or l2: 
            o1 = l1.val if l1 else 0
            o2 = l2.val if l2 else 0 

            total = carry + o1 + o2
            carry = total // 10 # get possible multi digit whole number
            total %= 10 # get single digit remainder
            

            curr.next = ListNode(total)
            curr = curr.next


            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next

        if carry > 0 :
            curr.next = ListNode(carry)

        return dummy.next