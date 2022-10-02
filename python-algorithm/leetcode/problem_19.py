"""19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Constraints:

  The number of nodes in the list is sz.
  1 <= sz <= 30
  0 <= Node.val <= 100
  1 <= n <= sz
"""
from typing import Optional
from common.list_node import ListNode


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast_ptr = dummy
        for i in range(n):
            fast_ptr = fast_ptr.next
        slow_ptr = dummy
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        for i in range(n):
            if not ptr:
                return None
            ptr = ptr.next
        dummy = pre = ListNode(-1, head)
        cur = head
        while ptr:
            ptr = ptr.next
            pre = cur
            cur = cur.next
        if cur:
            pre.next = cur.next
        return dummy.next
