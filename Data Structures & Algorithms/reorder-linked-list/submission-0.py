# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            holder = curr.next
            curr.next = prev
            prev = curr
            curr = holder

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        list1 = head
        list2 = self.reverseList(slow.next)
        slow.next = None
        
        while list1 and list2:
            holder1 = list1.next
            list1.next = list2
            holder2 = list2.next
            list2.next = holder1
            list1 = holder1
            list2 = holder2
        
            




        
        




