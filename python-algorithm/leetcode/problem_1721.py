"""1721. Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""
from typing import Optional

from common.list_node import ListNode


# 1 2 3 4
# 1 2 3
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        a, b = k, n - k + 1
        if a < b:
            a, b = b, a
        i = 0
        p = head
        node1, node2 = None, None
        while i < n:
            i += 1
            if i == a:
                node1 = p
            if i == b:
                node2 = p
            p = p.next
        node1.val, node2.val = node2.val, node1.val
        return head
