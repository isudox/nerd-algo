package main

import "sort"

// 148. Sort List
// https://leetcode.com/problems/sort-list/

func sortList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	treeMap := make(map[int][]*ListNode, 0)
	nums := make([]int, 0)
	ptr := head
	for ptr != nil {
		nums = append(nums, ptr.Val)
		if _, ok := treeMap[ptr.Val]; !ok {
			treeMap[ptr.Val] = make([]*ListNode, 0)
		}
		treeMap[ptr.Val] = append(treeMap[ptr.Val], ptr)
		ptr = ptr.Next
	}
	sort.Ints(nums)
	dummy := &ListNode{Val: -1, Next: nil}
	cur := dummy
	for _, num := range nums {
		for _, node := range treeMap[num] {
			cur.Next = node
			cur = node
		}
	}
	cur.Next = nil
	return dummy.Next
}
