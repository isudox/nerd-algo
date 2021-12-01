package main

// 198. House Robber
// https://leetcode.com/problems/house-robber/

func rob(nums []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	m := len(nums)
	dp := []int{0, nums[0]}
	for i := 1; i < m; i++ {
		notRob := max(dp[0], dp[1])
		rob := dp[0] + nums[i]
		dp[0] = notRob
		dp[1] = rob
	}
	return max(dp[0], dp[1])
}
