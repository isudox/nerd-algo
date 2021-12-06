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
}

func main() {
	// 1 2 3 4 5
	// 1 3 5
	var p1 = &ListNode{1, nil}
	var p2 = &ListNode{2, nil}
	var p3 = &ListNode{3, nil}
	var p4 = &ListNode{4, nil}
	var p5 = &ListNode{5, nil}
	p1.Next = p2
	p2.Next = p3
	p3.Next = p4
	p4.Next = p5
	ptr := p1
	oddEvenList(p1)
	for ptr != nil {
		println(ptr.Val)
		ptr = ptr.Next
	}
}
