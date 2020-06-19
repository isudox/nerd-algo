"""1028. Recover a Tree From Preorder Traversal
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node),
then we output the value of this node.
(If the depth of a node is D, the depth of its immediate child is D+1.
The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.


Example 1:
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]

Note:

The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9.
"""
from common.tree_node import TreeNode


class Solution:
    def recover_from_preorder(self, s: str) -> TreeNode:
        if not s:
            return None
        i = 0
        while i < len(s) and s[i] != '-':
            i += 1
        root = TreeNode(s[:i])
        store = [root]
        cur_depth, pre_depth = 0, -1
        while i < len(s):
            if s[i] == '-':
                cur_depth += 1
                i += 1
            else:
                j = i + 1
                while j < len(s) and s[j] != '-':
                    j += 1
                val = s[i: j]
                i = j
                cur_node = TreeNode(val)
                if cur_depth > pre_depth:
                    # cur node is the left sub node for the previous node
                    store[-1].left = cur_node
                else:
                    # cur node is the right sibling for the previous node
                    while cur_depth <= pre_depth:
                        store.pop()
                        pre_depth -= 1
                    store[-1].right = cur_node
                store.append(cur_node)
                pre_depth = cur_depth
                cur_depth = 0
        return root

    def recover_from_preorder_2(self, s: str) -> TreeNode:
        def add_node(value, depth, store):
            store[depth] = TreeNode(value)
            if depth == 0:
                return
            if not store[depth - 1].left:
                store[depth - 1].left = store[depth]
            else:
                store[depth - 1].right = store[depth]

        store = {}
        val = ''
        depth = 0
        for c in s:
            if c != '-':
                val += c
            elif val == '':
                depth += 1
            else:
                add_node(val, depth, store)
                val = ''
                depth = 1  # 当前 c = '-'，所以 depth 设置为 1
        add_node(val, depth, store)
        return store[0]
