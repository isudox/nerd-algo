package main

// 138. Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

func copyRandomList(head *RandomNode) *RandomNode {
	if head == nil {
		return nil
	}
	mapper := make(map[*RandomNode]*RandomNode)
	ptr := head
	for ptr != nil {
		node := &RandomNode{ptr.Val, nil, nil}
		mapper[ptr] = node
		ptr = ptr.Next
	}
	ptr = head
	for ptr != nil {
		next, random := ptr.Next, ptr.Random
		if next != nil {
			mapper[ptr].Next = mapper[next]
		}
		if random != nil {
			mapper[ptr].Random = mapper[random]
		}
		ptr = ptr.Next
	}
	return mapper[head]
}

type RandomNode struct {
	Val    int
	Next   *RandomNode
	Random *RandomNode
}
