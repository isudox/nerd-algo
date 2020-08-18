"""109. Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given the head of a singly linked list where elements are sorted in
ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

      0
     / \
   -3   9
   /   /
 -10  5
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
shown height balanced BST.
"""
from common.list_node import ListNode
from common.tree_node import TreeNode


class Solution:
    def sorted_list_to_bst(self, head: ListNode) -> TreeNode:
        def recur(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            mid = start + (end - start) // 2
            root = TreeNode(nums[mid])
            root.left = recur(start, mid - 1)
            root.right = recur(mid + 1, end)
            return root

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return recur(0, len(nums) - 1)

    def sorted_list_to_bst_2(self, head: ListNode) -> TreeNode:
        """fast and slow pointer"""
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        prev, p, q = None, head, head
        while q and q.next:
            prev = p
            p = p.next
            q = q.next.next
        root = TreeNode(p.val)
        right = p.next
        prev.next = None
        root.left = self.sorted_list_to_bst_2(head)
        root.right = self.sorted_list_to_bst_2(right)
        return root
