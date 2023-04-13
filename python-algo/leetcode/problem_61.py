"""61. Rotate List
https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""
from common.list_node import ListNode


class Solution:
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        p = head
        n = 0
        while p:
            p = p.next
            n += 1
        if n == 0:
            return head
        k = k % n
        if k == 0:
            return head
        ptr_fast, ptr_slow = head, head
        while ptr_fast.next:
            if k <= 0:
                ptr_slow = ptr_slow.next
            ptr_fast = ptr_fast.next
            k -= 1
        new_head = ptr_slow.next
        ptr_slow.next = None
        ptr_fast.next = head
        return new_head
