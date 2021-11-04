package main

// 404. Sum of Left Leaves
// https://leetcode.com/problems/sum-of-left-leaves/

func sumOfLeftLeaves(root *TreeNode) int {
	ans := 0
	var dfs func(node *TreeNode, isLeft bool)
	dfs = func(node *TreeNode, isLeft bool) {
		if node == nil {
			return
		}
		if node.Left == nil && node.Right == nil && isLeft {
			ans += node.Val
			return
		}
		if node.Left != nil {
			dfs(node.Left, true)
		}
		if node.Right != nil {
			dfs(node.Right, false)
		}
	}
	dfs(root, false)
	return ans
}
