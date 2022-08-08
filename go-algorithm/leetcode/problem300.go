package main

// 300. Longest Increasing Subsequence
// https://leetcode.cn/problems/longest-increasing-subsequence/

func lengthOfLIS(nums []int) int {
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	n := len(nums)
	dp := make([]int, n)
	stack := make([][]int, 0)
	ans := 0
	for i := 0; i < n; i++ {
		dp[i] = 1
		j := len(stack) - 1
		for j >= 0 && stack[j][0] < nums[i] {
			dp[i] = max(dp[i], dp[stack[j][1]]+1)
			j -= 1
		}
		if j == len(stack)-1 {
			stack = append(stack, []int{nums[i], i})
		} else {
			j += 1
			stack = append(stack[:j+1], stack[j:]...)
			stack[j] = []int{nums[i], i}
		}
		ans = max(ans, dp[i])
	}
	return ans
}
