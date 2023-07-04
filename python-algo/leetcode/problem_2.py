"""2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        add = 0
        while l1 and l2:
            add, val = divmod(l1.val + l2.val + add, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        l3 = l1 if l1 else l2
        while l3:
            if add == 0:
                cur.next = l3
                break
            add, val = divmod(l3.val + add, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l3 = l3.next
        if add:
            cur.next = ListNode(add)
        return dummy.next
