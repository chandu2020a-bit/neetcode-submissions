# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        count = 0 
        top = head 
        while top :
            length += 1 
            top = top.next 

        dumm = ListNode(0, head)
        top = dumm 

        while count < (length-n):
            top = top.next
            count += 1 

        top.next = top.next.next 
        return dumm.next
        