# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return[]
        result = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            temp = []
            
            for i in range(level_length):
                node = queue.popleft()
                temp.append(node.val)
                
                if i== level_length - 1:
                    result.append(temp)
                    
                # Add the left and right children (if they exist) to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

        