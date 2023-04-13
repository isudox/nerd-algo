package main

// 421. Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

func findMaximumXOR(nums []int) int {
	type Trie struct {
		kids [2]*Trie
	}
	insert := func(t *Trie, num int) {
		node := t
		for i := 30; i >= 0; i-- {
			bit := (num >> i) & 1
			if node.kids[bit] == nil {
				node.kids[bit] = &Trie{}
			}
			node = node.kids[bit]
		}
	}
	check := func(t *Trie, num int) int {
		node := t
		ret := 0
		for i := 30; i >= 0; i-- {
			bit := (num >> i) & 1
			ret = ret << 1
			if node.kids[1-bit] != nil {
				node = node.kids[1-bit]
				ret++
			} else {
				node = node.kids[bit]
			}
		}
		return ret
	}
	ans := 0
	trie := &Trie{}
	for i := 1; i < len(nums); i++ {
		insert(trie, nums[i-1])
		if cur := check(trie, nums[i]); cur > ans {
			ans = cur
		}
	}
	return ans
}
