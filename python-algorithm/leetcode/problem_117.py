"""117. Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not
count as extra space for this problem.
"""
from typing import List


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue, next_queue = [root], []
        while queue:
            node = queue.pop(0)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
            if queue:
                node.next = queue[0]
            else:
                queue = next_queue
                next_queue = []
        return root

    def connect_1(self, root: 'Node') -> 'Node':
        def bfs(q1: List[Node], q2: List[Node]):
            while q1:
                node = q1.pop(0)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
                if q1:
                    node.next = q1[0]
                else:
                    bfs(q2, q1)
        if root:
            bfs([root], [])
        return root


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
