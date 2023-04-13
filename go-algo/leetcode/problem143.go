package main

// 143. Reorder List
// https://leetcode.com/problems/reorder-list/

func reorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}
	stack := make([]*ListNode, 0)
	ptr := head
	for ptr != nil {
		stack = append(stack, ptr)
		ptr = ptr.Next
	}
	n := len(stack)
	var prev *ListNode
	for i := 0; i < n/2; i++ {
		if prev != nil {
			prev.Next = stack[i]
		}
		stack[i].Next = stack[n-1-i]
		prev = stack[n-1-i]
	}
	if n%2 == 0 {
		prev.Next = nil
	} else {
		prev.Next = stack[n/2]
		stack[n/2].Next = nil
	}
}
