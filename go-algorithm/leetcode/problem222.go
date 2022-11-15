package main

// 222. Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return countNodes(root.Left) + countNodes(root.Right) + 1
}
