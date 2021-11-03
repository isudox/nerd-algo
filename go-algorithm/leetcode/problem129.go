package main

// 129. Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

func sumNumbers(root *TreeNode) int {
	ans := 0
	var dfs func(node *TreeNode, num int)
	dfs = func(node *TreeNode, num int) {
		if node == nil {
			ans += num
			return
		}
		num = num*10 + node.Val
		if node.Left == nil && node.Right == nil {
			ans += num
		}
		if node.Left != nil {
			dfs(node.Left, num)
		}
		if node.Right != nil {
			dfs(node.Right, num)
		}
	}
	dfs(root, 0)
	return ans
}
