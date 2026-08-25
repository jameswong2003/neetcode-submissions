# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode()

        carryover = 0
        while l1 or l2 or carryover:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            total = l1_value + l2_value + carryover
            carryover = total // 10

            curr.next = ListNode(total % 10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next