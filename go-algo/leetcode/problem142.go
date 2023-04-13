package main

// 142. Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	slow, fast := head, head
	steps := 0
	found := false
	for slow != nil && fast != nil {
		if slow.Next != nil && fast.Next != nil && fast.Next.Next != nil {
			slow = slow.Next
			fast = fast.Next.Next
			steps++
			if slow == fast {
				found = true
				break
			}
		} else {
			return nil
		}
	}
	if !found {
		return nil
	}
	ptr1, ptr2 := head, head
	for i := 0; i < steps; i++ {
		ptr1 = ptr1.Next
	}
	for ptr1 != ptr2 {
		ptr1 = ptr1.Next
		ptr2 = ptr2.Next
	}
	return ptr1
}
