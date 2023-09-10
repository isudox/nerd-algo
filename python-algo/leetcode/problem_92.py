"""92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node: ListNode) -> ListNode:
            prev = None
            while node:
                curr = node
                node = node.next
                curr.next = prev
                prev = curr
            return prev

        if not head or not head.next or left == right:
            return head
        dummy = ptr = ListNode(0, head)
        start = end = ptr
        i = 0
        while ptr:
            if i == left - 1:
                start = ptr
            if i == right:
                end = ptr.next
                ptr.next = None
            ptr = ptr.next
            i += 1
        old_start = start.next
        new_start = reverse(start.next)
        start.next = new_start
        old_start.next = end
        return dummy.next
