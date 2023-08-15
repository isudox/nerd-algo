"""86. Partition List
https://leetcode.com/problems/partition-list/
"""
from common.list_node import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        left = left_start = ListNode(0)
        right = right_start = ListNode(0)
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = right_start.next
        return left_start.next
