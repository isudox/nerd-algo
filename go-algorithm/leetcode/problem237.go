package main

// 237. Delete Node in a Linked List
// https://leetcode.com/problems/delete-node-in-a-linked-list/

func deleteNode(node *ListNode) {
	node.Val = node.Next.Val
	node.Next = node.Next.Next
}
