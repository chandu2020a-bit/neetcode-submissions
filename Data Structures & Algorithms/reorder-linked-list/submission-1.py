# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        nodes_arr = []
        curr = head
        while curr:
            nodes_arr.append(curr)
            curr = curr.next
            
        left = 0
        right = len(nodes_arr) - 1
        
        while left < right:
            nodes_arr[left].next = nodes_arr[right]
            left += 1

            if left >= right:
                break

            nodes_arr[right].next = nodes_arr[left]
            right -= 1

        nodes_arr[left].next = None