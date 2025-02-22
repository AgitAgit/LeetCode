class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start_node = None
        current_list = None

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            start_node = list1
            list1 = list1.next
            current_list = 1
        else:
            start_node = list2
            list2 = list2.next
            current_list = 2

        result = start_node

        while start_node.next:
            print("start",start_node.val)
            print("list1", list1.val)
            print("list2", list2.val)

            if start_node.next.val > list1.val:
                start_node.next = list1
                list1 = list1.next
                current_list = 1
            elif start_node.next.val > list2.val:
                start_node.next = list2
                list2 = list2.next
                current_list = 2
            elif current_list == 1:
                start_node.next = list1
                list1 = list1.next
            elif current_list == 2:
                start_node.next = list2
                list2 = list2.next
            start_node = start_node.next
            
        if list1 is not None:
            start_node.next = list1
        else:
            start_node.next = list2

        return result