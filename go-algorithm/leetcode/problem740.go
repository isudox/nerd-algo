package main

import "sort"

// 740. Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

func deleteAndEarn(nums []int) int {
	sort.Ints(nums)
	dp := []int{0, nums[0]}
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			dp[1] += nums[i]
		} else if nums[i] == nums[i-1]+1 {
			tmp := dp[0]
			dp[0] = max(dp[0], dp[1])
			dp[1] = tmp + nums[i]
		} else {
			dp[0] = max(dp[0], dp[1])
			dp[1] = dp[0] + nums[i]
		}
	}
	return max(dp[0], dp[1])
}
