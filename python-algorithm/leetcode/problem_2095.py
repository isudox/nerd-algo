"""2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""
from typing import Optional

from common.list_node import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        m = n // 2
        dummy = ListNode(0, next=head)
        pre, cur = dummy, head
        while m:
            pre = cur
            cur = cur.next
            m -= 1
        pre.next = cur.next
        return dummy.next

