# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = None
        index = 0
        while fast:
            if index == n :
                slow = head
            elif slow:
                slow = slow.next
            fast = fast.next
            index += 1

        if slow:
            slow.next = slow.next.next
        else:
            head = head.next

        return head