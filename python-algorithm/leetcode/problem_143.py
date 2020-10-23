"""143. Reorder List
https://leetcode.com/problems/reorder-list/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes,
only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
from common.list_node import ListNode


class Solution:
    def reorder_list(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        store = [head]
        p = head
        while p.next:
            store.append(p.next)
            p = p.next
        n = len(store)
        prev = None
        for i in range(n // 2):
            if prev:
                prev.next = store[i]
            store[i].next = store[n - 1 - i]
            prev = store[n - 1 - i]
        if divmod(n, 2) == 0:
            prev.next = None
        else:
            prev.next = store[n // 2]
            store[n // 2].next = None
