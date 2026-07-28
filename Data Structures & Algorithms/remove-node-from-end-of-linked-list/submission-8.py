# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        slow = dummy 
        fast = dummy 


        # keep an n + 1 (we want the node before n) sized window from the beginning 
        for i in range(n+1):
            fast = fast.next

        while fast: 
            slow = slow.next
            fast = fast.next

        # slow is currently now before the nth node 
        slow.next = slow.next.next


        return dummy.next
