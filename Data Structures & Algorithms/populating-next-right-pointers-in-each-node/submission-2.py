"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque([root])
        
        while len(queue) > 0:
            len_queue = len(queue)

            while len_queue:
                el = queue.popleft()
                if len_queue > 1:
                   el.next = queue[0]

                if el.left:
                    queue.append(el.left)

                if el.right:
                    queue.append(el.right)

                len_queue -= 1

        return root

                