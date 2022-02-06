package main

// 23. Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

func mergeKLists(lists []*ListNode) *ListNode {
	merge := func(l1, l2 *ListNode) *ListNode {
		dummy := &ListNode{0, nil}
		cur := dummy
		for l1 != nil || l2 != nil {
			if l1 == nil {
				cur.Next = l2
				break
			}
			if l2 == nil {
				cur.Next = l1
				break
			}
			if l1.Val < l2.Val {
				cur.Next = l1
				l1 = l1.Next
			} else {
				cur.Next = l2
				l2 = l2.Next
			}
			cur = cur.Next
		}
		return dummy.Next
	}
	if lists == nil || len(lists) == 0 {
		return nil
	}
	ans := lists[0]
	for i := 1; i < len(lists); i++ {
		ans = merge(ans, lists[i])
	}
	return ans
}
