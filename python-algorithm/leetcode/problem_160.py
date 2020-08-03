"""160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Write a program to find the node at which the intersection of two singly
linked lists begins.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
