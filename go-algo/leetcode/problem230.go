package main

// 230. Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

func kthSmallest(root *TreeNode, k int) int {
	var stack []*TreeNode
	enq := func(node *TreeNode) {
		for node != nil {
			stack = append(stack, node)
			node = node.Left
		}
	}
	enq(root)
	node := stack[len(stack)-1]
	for k > 0 {
		node = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		k--
		if node.Right != nil {
			enq(node.Right)
		}
	}
	return node.Val
}
