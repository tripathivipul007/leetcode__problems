# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copytoold = {None: None}
        
        # First pass: Create all nodes without setting next and random pointers
        curr = head
        while curr:
            copy = Node(curr.val)
            copytoold[curr] = copy
            curr = curr.next
        
        # Second pass: Assign next and random pointers
        curr = head
        while curr:
            copy = copytoold[curr]
            copy.next = copytoold[curr.next]
            copy.random = copytoold[curr.random]
            curr = curr.next
        
        return copytoold[head]
