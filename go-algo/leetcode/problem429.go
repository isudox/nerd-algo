package main

// 429. N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

func levelOrder(root *Node429) [][]int {
	ans := make([][]int, 0)
	if root == nil {
		return ans
	}
	q := []*Node429{root}
	for len(q) > 0 {
		n := len(q)
		level := make([]int, 0)
		for i := 0; i < n; i++ {
			node := q[0]
			level = append(level, node.Val)
			q = q[1:]
			for _, child := range node.Children {
				q = append(q, child)
			}
		}
		ans = append(ans, level)
	}
	return ans
}

type Node429 struct {
	Val      int
	Children []*Node429
}
