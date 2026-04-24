# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        while head and head.next != None:
            head.val = 'visited'
            head = head.next
            if head.val == 'visited':
                return True

        return False
        