# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            start = list1
            list1 = list1.next
        else:
            start = list2
            list2 = list2.next

        result = start

        while list1 and list2 and start:
            if list1.val <= list2.val:
                start.next = list1
                list1 = list1.next
            else:
                start.next = list2
                list2 = list2.next
            start = start.next
        if start and list1:#suppose list has reached it's end
            start.next = list1
        elif start:
            start.next = list2

        return result