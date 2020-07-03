"""206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


Follow up:

A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""
from common.list_node import ListNode


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        """
        iteratively.
        time complexity: O(N)
        space complexity: O(1)
        :param head:
        :return:
        """
        # iteratively.
        if head is None or head.next is None:
            return head
        p1, p2 = None, head
        while p2 is not None:
            next_node = p2.next
            p2.next = p1
            p1 = p2
            p2 = next_node
        return p1

    def reverse_list1(self, head: ListNode) -> ListNode:
        """
        recursively.
        time complexity: O(N)
        space complexity: O(N)
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head
        ans, p = head, head
        next_node = p.next
        p.next = None
        ans = self.reverse_list1(next_node)
        next_node.next = p
        return ans

    def reverse_list2(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        store = []
        while head is not None:
            store.append(ListNode(head.val))
            head = head.next
        for i in range(len(store) - 1, 0, -1):
            store[i].next = store[i - 1]
        return store[-1]
