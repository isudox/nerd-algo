package main

// 55. Jump Game
// https://leetcode.com/problems/jump-game/

func canJump(nums []int) bool {
	n := len(nums)
	store := make(map[int]bool)
	store[n-1] = true
	for i := n - 2; i >= 0; i-- {
		for k := range store {
			if k-i <= nums[i] {
				store[i] = true
				break
			}
		}
	}
	return store[0]
}
