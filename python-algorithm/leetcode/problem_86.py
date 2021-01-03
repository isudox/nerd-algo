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
        left_store, right_store = [], []
        ptr = head
        while ptr:
            if ptr.val < x:
                left_store.append(ptr)
            else:
                right_store.append(ptr)
            ptr = ptr.next
        for i in range(len(left_store)):
            if i == len(left_store) - 1:
                left_store[i].next = None
            else:
                left_store[i].next = left_store[i + 1]
        for i in range(len(right_store)):
            if i == len(right_store) - 1:
                right_store[i].next = None
            else:
                right_store[i].next = right_store[i + 1]
        ans = left_store[0] if left_store else right_store[0]
        if left_store and right_store:
            left_store[-1].next = right_store[0]
        return ans
