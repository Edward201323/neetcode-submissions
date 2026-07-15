# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr_dummy = dummy
        curr_list1 = list1
        curr_list2 = list2
        while curr_list1 is not None and curr_list2 is not None:
            if curr_list1.val < curr_list2.val:
                curr_dummy.next = curr_list1
                curr_list1 = curr_list1.next
            else:
                curr_dummy.next = curr_list2
                curr_list2 = curr_list2.next
            curr_dummy = curr_dummy.next
        
        if curr_list1 is not None:
            curr_dummy.next = curr_list1
        elif curr_list2 is not None:
            curr_dummy.next = curr_list2
        
        return dummy.next