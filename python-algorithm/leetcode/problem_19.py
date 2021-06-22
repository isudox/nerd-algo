"""19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
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
