"""968. Binary Tree Cameras
https://leetcode.com/problems/binary-tree-cameras/

Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
    <>
   /
  <O>
  /\
<>  <>
Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Input: [0,0,null,0,null,0,null,null,0]
       <>
      /
     <O>
     /
    <>
    /
   <O>
    \
    <>
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree.
The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""
from common.tree_node import TreeNode


class Solution:
    def min_camera_cover(self, root: TreeNode) -> int:
        return 0
