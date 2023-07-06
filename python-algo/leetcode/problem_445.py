"""445. Add Two Numbers II
https://leetcode.com/problems/add-two-numbers-ii/
"""
from common.list_node import ListNode
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node: ListNode) -> int:
            ret = 0
            while node:
                ret = ret * 10 + node.val
                node = node.next
            return ret

        if not l1:
            return l2
        if not l2:
            return l1
        val = str(helper(l1) + helper(l2))
        dummy = ListNode(0)
        p = dummy
        for c in val:
            p.next = ListNode(int(c))
            p = p.next
        return dummy.next
