package leetcode

// 437. Path Sum III
// https://leetcode.com/problems/path-sum-iii/

func pathSum(root *TreeNode, targetSum int) int {
	if root == nil {
		return 0
	}
	var dfs func(node *TreeNode, target int) int
	dfs = func(node *TreeNode, target int) int {
		if node == nil {
			return 0
		}
		ret := 0
		if node.Val == target {
			ret++
		}
		return ret + dfs(node.Left, target-node.Val) + dfs(node.Right, target-node.Val)
	}
	return dfs(root, targetSum) + pathSum(root.Left, targetSum) + pathSum(root.Right, targetSum)
}
