# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        # The first element of preorder list is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find the index of the root in inorder list
        inorder_index = inorder.index(root_val)

        # Recursively build the left and right subtrees
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        

        return root