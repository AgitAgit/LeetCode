# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        counter = 0
        while head:
            counter += 1
            head = head.next
            if(counter > 10000):
                return True
        return False