# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Compute the length of the list
        length = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        # Connect the last node to the head to make it circular
        old_tail.next = head
        
        # Find the new tail: (length - k % length - 1)th node
        # and the new head: (length - k % length)th node
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # Break the circle
        new_tail.next = None
        
        return new_head
                    
                
            
            
        