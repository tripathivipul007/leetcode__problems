# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        # First pass to count occurrences
        count = {}
        current = head
        while current:
            count[current.val] = count.get(current.val, 0) + 1
            current = current.next

        # Dummy node to handle edge cases where head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        # Second pass to remove all nodes with count > 1
        while current:
            if count[current.val] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next