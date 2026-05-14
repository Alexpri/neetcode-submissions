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
            additional_queue = deque([])

            for i in range(len_queue):
                el = queue.popleft()
                if len(queue) != 0:
                   el.next = queue[0]

                if el.left:
                    additional_queue.append(el.left)

                if el.right:
                    additional_queue.append(el.right)

            queue.extend(additional_queue)

        return root

                