"""24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/
"""
from common.list_node import ListNode


def swap_pairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    cur = head
    nxt = head.next
    nxt_nxt = nxt.next
    nxt.next = cur
    cur.next = swap_pairs(nxt_nxt)
    return nxt
