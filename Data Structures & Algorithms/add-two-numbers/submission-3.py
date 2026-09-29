# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        head = l1
        sec_head = l2
        
        # Loop continues if there are remaining nodes OR a carry left to add
        while head or sec_head or carry:
            # Extract values, default to 0 if one list finishes early
            val1 = head.val if head else 0
            val2 = sec_head.val if sec_head else 0
            
            # Calculate total sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the single-digit remainder
            curr.next = ListNode(total % 10)
            
            # Advance pointers
            curr = curr.next
            if head:
                head = head.next
            if sec_head:
                sec_head = sec_head.next
                
        # Return the actual head of the resulting linked list
        return dummy.next