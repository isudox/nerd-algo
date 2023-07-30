"""143. Reorder List
https://leetcode.com/problems/reorder-list/
"""
from common.list_node import ListNode


class Solution:
    def reorder_list(self, head: ListNode) -> None:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        i, j = 0, len(nodes) - 1
        pre = None
        while i <= j:
            if pre:
                pre.next = nodes[i]
            nodes[i].next = nodes[j]
            nodes[j].next = None
            pre = nodes[j]
            i += 1
            j -= 1
