# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # The first element of preorder list is the root
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        # Find the index of the root in inorder list
        inorder_index = inorder.index(root_val)

        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index + 1:])

        return root