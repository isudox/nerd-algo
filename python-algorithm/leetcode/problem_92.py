"""92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""
from common.list_node import ListNode


class Solution:
    def reverse_between(self, head: ListNode, left: int, right: int) -> ListNode:
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
