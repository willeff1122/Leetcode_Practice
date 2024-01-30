# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next == head:
                prev = prev.next
                head = head.next
            else:
                prev.next = head.next
                head = prev.next
        return dummy.next
