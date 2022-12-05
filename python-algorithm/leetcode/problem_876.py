"""876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
"""
from common.list_node import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        n = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            n += 1
        n = n // 2
        ptr = head
        while n:
            ptr = ptr.next
            n -= 1
        return ptr
