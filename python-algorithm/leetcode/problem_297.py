"""297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm
should work. You just need to ensure that a binary tree can be serialized
to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a
binary tree. You do not necessarily need to follow this format, so please
be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
"""

from common.tree_node import TreeNode


class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return '[]'
        queue = [root]
        store = []
        while queue:
            node = queue.pop(0)
            value = None if not node else node.val
            store.append(str(value))
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return '[' + ','.join(store) + ']'

    def deserialize(self, data: str) -> TreeNode:
        nums = (data[1: len(data) - 1])
        if nums == '':
            return None
        nums = nums.split(',')
        ans = TreeNode(nums.pop(0))
        queue = [ans]
        i = 1
        while nums:
            node = queue.pop(0)
            val = nums.pop(0)
            if val != 'None':
                node.left = TreeNode(val)
                queue.append(node.left)
            i += 1
            if not nums:
                break
            val = nums.pop(0)
            if val != 'None':
                node.right = TreeNode(val)
                queue.append(node.right)
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
