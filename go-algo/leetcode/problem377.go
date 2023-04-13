package main

import "sort"

// 377. Combination Sum IV
// https://leetcode.com/problems/combination-sum-iv/

func combinationSum4(nums []int, target int) int {
	sort.Ints(nums)
	dp := make([]int, target+1)
	dp[0] = 1
	for i := 1; i <= target; i++ {
		for _, num := range nums {
			if num > i {
				break
			}
			dp[i] += dp[i-num]
		}
	}
	return dp[target]
}
