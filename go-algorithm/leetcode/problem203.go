package main

// 203. Remove Linked List Elements
// https://leetcode.com/problems/remove-linked-list-elements/

func removeElements(head *ListNode, val int) *ListNode {
	dummy := &ListNode{-1, head}
	pre, ptr := dummy, head
	for ptr != nil {
		if ptr.Val == val {
			ptr = ptr.Next
			pre.Next = ptr
		} else {
			pre = ptr
			ptr = ptr.Next
		}
	}
	return dummy.Next
}
