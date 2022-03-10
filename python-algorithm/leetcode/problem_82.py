"""82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""
import collections
from typing import Optional

from common.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(head.val - 1)
        pre = dummy
        cur = head
        while cur:
            if cur.next:
                if cur.val != pre.val and cur.val != cur.next.val:
                    pre.next = cur
                    cur = cur.next
                    pre = pre.next
                    pre.next = None
                else:
                    val = cur.val
                    while cur and cur.val == val:
                        cur = cur.next
            else:
                pre.next = cur
                cur = cur.next
        return dummy.next
