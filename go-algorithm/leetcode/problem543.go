package leetcode

// 543. Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

func diameterOfBinaryTree(root *TreeNode) int {
	ans := 0
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	var helper func(node *TreeNode) (ret [2]int)
	helper = func(node *TreeNode) (ret [2]int) {
		if node.Left == nil {
			ret[0] = 0
		} else {
			next := helper(node.Left)
			ret[0] = max(next[0], next[1]) + 1
		}
		if node.Right == nil {
			ret[1] = 0
		} else {
			next := helper(node.Right)
			ret[1] = max(next[0], next[1]) + 1
		}
		if sum := ret[0] + ret[1]; sum > ans {
			ans = sum
		}
		return ret
	}
	helper(root)
	return ans
}
