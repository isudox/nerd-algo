"""148. Sort List
https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
from common.list_node import ListNode


class Solution:
    def sort_list(self, head: ListNode) -> ListNode:
        def merge_sorted_list(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val <= l2.val:
                merged_list = l1
                merged_list.next = merge_sorted_list(l1.next, l2)
            else:
                merged_list = l2
                merged_list.next = merge_sorted_list(l1, l2.next)
            return merged_list

        def get_middle_node(l: ListNode) -> ListNode:
            if not l:
                return l
            slow_ptr = l
            fast_prt = l.next
            while fast_prt:
                fast_prt = fast_prt.next
                if fast_prt:
                    fast_prt = fast_prt.next
                    slow_ptr = slow_ptr.next
            return slow_ptr

        if not head or not head.next:
            return head
        middle_mode = get_middle_node(head)
        right_list = middle_mode.next
        middle_mode.next = None
        left_sorted_list = self.sort_list(head)
        right_sorted_list = self.sort_list(right_list)

        return merge_sorted_list(left_sorted_list, right_sorted_list)
