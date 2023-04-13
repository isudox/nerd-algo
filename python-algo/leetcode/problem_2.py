"""2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
