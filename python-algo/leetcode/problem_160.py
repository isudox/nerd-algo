"""160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB, return the node
at which the two lists intersect. If the two linked lists have no
intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

It is guaranteed that there are no cycles anywhere in the entire linked
structure.

Note that the linked lists must retain their original structure after the
function returns

Write a program to find the node at which the intersection of two singly
linked lists begins.

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
0 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB
intersect.

Follow up: Could you write a solution that runs in O(n) time and use only
O(1) memory?
"""
from common.list_node import ListNode


class Solution:
    def get_intersection_node(self, a: ListNode, b: ListNode) -> ListNode:
        if not a or not b:
            return None
        p_a, p_b = a, b
        while p_a != p_b:
            p_a = p_a.next if p_a else b
            p_b = p_b.next if p_b else a
        return p_a

    def get_intersection_node2(self, a: ListNode, b: ListNode) -> ListNode:
        def helper(short_node: ListNode, long_node: ListNode, ptr: ListNode) -> ListNode:
            diff = 0
            while ptr:
                diff += 1
                ptr = ptr.next
            ptr_long, ptr_short = long_node, short_node
            while diff:
                ptr_long = ptr_long.next
                diff -= 1
            while ptr_long != ptr_short:
                ptr_long = ptr_long.next
                ptr_short = ptr_short.next
            return ptr_long

        if not a or not b:
            return None
        pa, pb = a, b
        while pa and pb:
            pa = pa.next
            pb = pb.next
        if pa:
            return helper(b, a, pa)
        else:
            return helper(a, b, pb)
