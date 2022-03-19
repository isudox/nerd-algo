package main

// 328. Odd Even Linked List
// https://leetcode.com/problems/odd-even-linked-list/
// 1, 2, 3, 4
// 1, 3, 2, 4

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	p1, p2 := head, head.Next
	for p1 != nil && p2 != nil {
		p1.Next = p2.Next
		if p2.Next != nil {
			p2.Next = p2.Next.Next
		}
		p1 = p1.Next
	}
	return nil
}
