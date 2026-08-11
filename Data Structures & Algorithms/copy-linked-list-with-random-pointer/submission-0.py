"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Dictionary to map original nodes to their cloned copies
        # Maps None -> None to cleanly handle null pointers
        old_to_new = {None: None}
        
        # Step 1: Create a copy of all nodes and store in the map
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Step 2: Connect next and random pointers for the copied nodes
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next
            
        # Return the head of the newly copied linked list
        return old_to_new[head]