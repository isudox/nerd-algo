"""141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""
from common.list_node import ListNode


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
