"""147. Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/

Algorithm of Insertion Sort:

    Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
from common.list_node import ListNode


class Solution:
    def insertion_sort_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        start = ListNode(0)
        while head:
            ptr = start
            while ptr.next and ptr.next.val < head.val:
                ptr = ptr.next
            cur = head
            head = head.next
            cur.next = ptr.next
            ptr.next = cur
        return start.next
