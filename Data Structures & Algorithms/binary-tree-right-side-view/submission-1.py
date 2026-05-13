# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = [root.val]
        queue = deque([root])

        while len(queue) > 0:
            for i in range(len(queue)):
                current = queue.popleft()

                if current.right:
                    queue.append(current.right)
                
                if current.left:
                    queue.append(current.left)

            if len(queue):
                result.append(queue[0].val)

        return result



