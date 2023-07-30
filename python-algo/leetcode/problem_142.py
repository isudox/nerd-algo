"""142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
"""
from typing import Optional

from common.list_node import ListNode


def detect_cycle_1(head: ListNode) -> Optional[ListNode]:
    """
    Use extra space to record node.
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


def detect_cycle_2(head: ListNode) -> Optional[ListNode]:
    """
    Without using extra space
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


def detect_cycle_3(head: ListNode) -> Optional[ListNode]:
    """
    Good method of using math
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
