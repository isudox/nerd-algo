"""141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
Can you solve it using O(1) (i.e. constant) memory?
"""
from common.list_node import ListNode


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        p1, p2 = head, head
        while p2:
            p1 = p1.next
            p2 = p2.next
            if not p2:
                return False
            p2 = p2.next
            if p1 == p2:
                return True
        return False
