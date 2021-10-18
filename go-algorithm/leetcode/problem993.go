package leetcode

func isCousins(root *TreeNode, x int, y int) bool {
	store := make(map[int]int)
	var queue []*TreeNode
	queue = append(queue, root)
	depth := 0
	for len(queue) > 0 {
		n := len(queue)
		for i := 0; i < n; i++ {
			node := queue[0]
			queue = queue[1:]
			if node.Left != nil && node.Right != nil {
				if (node.Left.Val == x && node.Right.Val == y) || (node.Left.Val == y && node.Right.Val == x) {
					return false
				}
			}
			store[node.Val] = depth
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		depth++
	}
	return store[x] == store[y]
}
