package main

// 938. Range Sum of BST
// https://leetcode.com/problems/range-sum-of-bst/

func rangeSumBST(root *TreeNode, low int, high int) int {
	if root == nil {
		return 0
	}
	if root.Val > high {
		return rangeSumBST(root.Left, low, high)
	}
	if root.Val < low {
		return rangeSumBST(root.Right, low, high)
	}
	return root.Val + rangeSumBST(root.Left, low, high) + rangeSumBST(root.Right, low, high)
}
