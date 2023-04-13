package main

// 1008. Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

func bstFromPreorder(preorder []int) *TreeNode {
	if preorder == nil && len(preorder) == 0 {
		return nil
	}
	root := &TreeNode{preorder[0], nil, nil}
	i := 1
	for i < len(preorder) && preorder[i] < preorder[0] {
		i++
	}
	if i > 1 {
		root.Left = bstFromPreorder(preorder[1:i])
	}
	if i < len(preorder) {
		root.Right = bstFromPreorder(preorder[i:])
	}
	return root
}
