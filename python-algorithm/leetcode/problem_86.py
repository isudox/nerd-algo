"""86. Partition List
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
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
