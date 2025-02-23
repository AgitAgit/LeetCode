# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#This works because the question constrained the linked list to a maximum length of 10^4
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        counter = 0
        while head:
            counter += 1
            head = head.next
            if(counter > 10000):
                return True
        return False