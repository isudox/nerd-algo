"""1669. Merge In Between Linked Lists
https://leetcode.com/problems/merge-in-between-linked-lists/
"""
from common.list_node import ListNode


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = list2
        while tail.next:
            tail = tail.next
        i = 0
        ptr = list1
        left, right = None, None
        while ptr:
            if i == a - 1:
                left = ptr
            if i == b:
                right = ptr
                break
            ptr = ptr.next
            i += 1
        left.next = list2
        tail.next = right.next
        return list1
