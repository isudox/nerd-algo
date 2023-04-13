package main

// 337. House Robber III
// https://leetcode.com/problems/house-robber-iii/

func rob3(root *TreeNode) int {
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	memo0 := map[*TreeNode]int{}
	memo1 := map[*TreeNode]int{}
	memo := [2]map[*TreeNode]int{memo0, memo1}
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, can int) int {
		if node == nil {
			return 0
		}
		if memo[can][node] > 0 {
			return memo[can][node]
		}
		ret := dfs(node.Left, 1) + dfs(node.Right, 1)
		if can > 0 {
			ret = max(ret, node.Val+dfs(node.Left, 0)+dfs(node.Right, 0))
		}
		memo[can][node] = ret
		return ret
	}
	return dfs(root, 1)
}
