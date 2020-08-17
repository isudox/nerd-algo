"""142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the
second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the
first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def detect_cycle_1(self, head: ListNode) -> Optional[ListNode]:
        """
        Use extra space to record node.
        :param head:
        :return:
        """
        if not head:
            return None
        checked = {}
        p = ListNode(0)
        p.next = head
        while p:
            p = p.next
            if not p:
                return None
            if p in checked:
                return p
            checked[p] = 1

    def detect_cycle_2(self, head: ListNode) -> Optional[ListNode]:
        """
        Without using extra space
        :param head:
        :return:
        """
        if not head:
            return None
        p1, p2 = head, head
        cycle_len = 0
        meet_times = 0

        while p2:
            if meet_times == 1:
                cycle_len += 1
            p1 = p1.next
            p2 = p2.next
            if not p2 or not p2.next:
                return None
            p2 = p2.next
            if p1 == p2:
                meet_times += 1
            if meet_times == 2:
                break
        while head:
            entry = head
            for i in range(cycle_len):
                entry = entry.next
            if entry == head:
                return entry
            else:
                head = head.next

    def detect_cycle_3(self, head: ListNode) -> Optional[ListNode]:
        """
        Good method of using math
        :param head:
        :return:
        """
        if not head:
            return None
        p1 = p2 = head
        while p2:
            p1 = p1.next
            p2 = p2.next
            if not p2 or not p2.next:
                return None
            p2 = p2.next
            if p1 == p2:
                break
        if p2 == head:
            return head
        while p2 != head:
            head = head.next
            p2 = p2.next
        return head
