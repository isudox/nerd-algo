package main

// 430. Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

func flatten(root *Node) *Node {
	var dfs func(node *Node) (last *Node)
	dfs = func(node *Node) (last *Node) {
		ptr := node
		for ptr != nil {
			next := ptr.Next
			if ptr.Child != nil {
				child := dfs(ptr.Child)
				next = ptr.Next
				ptr.Next = ptr.Child
				ptr.Child.Prev = ptr
				if next != nil {
					child.Next = next
					next.Prev = child
				}
				ptr.Child = nil
				last = child
			} else {
				last = ptr
			}
			ptr = ptr.Next
		}
		return
	}
	dfs(root)
	return root
}

type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}
