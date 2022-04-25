package main

// 725. Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

func splitListToParts(head *ListNode, k int) []*ListNode {
	n := 0
	ptr := head
	for ptr != nil {
		ptr = ptr.Next
		n++
	}
	avg := n / k
	rem := n % k
	ans := make([]*ListNode, k)
	ptr = head
	for i := 0; i < k; i++ {
		node := ptr
		cnt := 0
		for ptr != nil {
			cnt++
			if (i < rem && cnt == avg+1) || (i >= rem && cnt == avg) {
				next := ptr.Next
				ptr.Next = nil
				ptr = next
				break
			} else {
				ptr = ptr.Next
			}
		}
		ans[i] = node
	}
	return ans
}
