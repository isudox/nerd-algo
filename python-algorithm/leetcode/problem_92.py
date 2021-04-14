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
        def helper(node: ListNode) -> ListNode:
            if node is None or node.next is None:
                return node
            p1, p2 = None, node
            while p2 is not None:
                next_node = p2.next
                p2.next = p1
                p1 = p2
                p2 = next_node
            return p1
