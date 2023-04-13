package main

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := ListNode{-1, nil}
	p1, p2, p3 := l1, l2, &dummy
	carry := 0
	for p1 != nil && p2 != nil {
		value := p1.Val + p2.Val + carry
		value, carry = value%10, value/10
		node := ListNode{value, nil}
		p3.Next = &node
		p1 = p1.Next
		p2 = p2.Next
		p3 = p3.Next
	}
	if p1 != nil {
		p3.Next = helper(p1, carry)
	} else if p2 != nil {
		p3.Next = helper(p2, carry)
	} else if carry == 1 {
		p3.Next = &ListNode{1, nil}
	}
	return dummy.Next
}

func helper(node *ListNode, carry int) *ListNode {
	if carry == 0 {
		return node
	}
	ptr := node
	for ptr != nil {
		ptr.Val += carry
		if ptr.Val < 10 {
			break
		}
		ptr.Val, carry = ptr.Val%10, ptr.Val/10
		if ptr.Next == nil && carry == 1 {
			ptr.Next = &ListNode{1, nil}
			break
		}
		ptr = ptr.Next
	}
	return node
}
