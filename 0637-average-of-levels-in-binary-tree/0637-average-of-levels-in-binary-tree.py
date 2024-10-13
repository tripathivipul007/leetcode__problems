# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            temp = 0

            # Traverse through all nodes at the current level
            for i in range(level_length):
                node = queue.popleft()

                temp +=node.val

                # If it's the last node of the current level, add it to the result
                if i == level_length - 1:
                    temp = temp/level_length
                    result.append(temp)

                # Add the left and right children (if they exist) to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
        