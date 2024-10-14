# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        result = []
        left_to_right = True
        
        while queue:
            level_length = len(queue)
            level = []
            
            for i in range(level_length):
                node = queue.popleft()
                
                if left_to_right:
                    level.append(node.val)
                    
                else:
                    level.insert(0,node.val)
                    
                if i== level_length-1:
                    result.append(level)
                    left_to_right = not left_to_right
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
        return result
                    
                    
            