# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_pointer = list1
        list2_pointer = list2

        current = dummy = ListNode(0, None)
        
        while list1_pointer and list2_pointer:
            if list1_pointer.val <= list2_pointer.val:
                current.next = list1_pointer
                list1_pointer = list1_pointer.next
            else:
                current.next = list2_pointer
                list2_pointer = list2_pointer.next
            current = current.next

        if list1_pointer:
            current.next = list1_pointer
        elif list2_pointer:
            current.next = list2_pointer
        
        return dummy.next