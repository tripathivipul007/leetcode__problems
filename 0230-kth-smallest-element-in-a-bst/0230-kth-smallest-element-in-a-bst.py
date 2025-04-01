# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inordertra = []
        def inordertraversal(root, lst):
            if root:
                inordertraversal(root.left,lst)
                lst.append(root.val)
                inordertraversal(root.right,lst)
            return lst
        return inordertraversal(root,inordertra)[k-1]

            
                