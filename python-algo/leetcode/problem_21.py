"""21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = dummy = ListNode(0)
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val <= p2.val:
                ptr.next = p1
                p1 = p1.next
            else:
                ptr.next = p2
                p2 = p2.next
            ptr = ptr.next
        if p1:
            ptr.next = p1
        elif p2:
            ptr.next = p2
        return dummy.next
