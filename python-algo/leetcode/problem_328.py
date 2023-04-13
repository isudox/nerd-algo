"""328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/

Given a singly linked list, group all odd nodes together followed by
the even nodes. Please note here we are talking about the node number
and not the value in the nodes.

You should try to do it in place. The program should run in O(1)
space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Constraints:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
    The length of the linked list is between [0, 10^4].
"""
from common.list_node import ListNode


class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        odd_ptr, even_ptr, joint = head, head.next, head.next
        while odd_ptr.next and even_ptr.next:
            odd_ptr.next = even_ptr.next
            odd_ptr = even_ptr.next
            if even_ptr.next.next:
                even_ptr.next = even_ptr.next.next
                even_ptr = odd_ptr.next
            else:
                even_ptr.next = None
                break
        odd_ptr.next = joint
        return head
