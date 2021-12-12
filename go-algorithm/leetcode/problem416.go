package main

import "sort"

// 416. Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/

func canPartition(nums []int) bool {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum%2 == 1 {
		return false
	}
	sort.Slice(nums, func(x, y int) bool {
		return nums[x] < nums[y]
	})
	target := sum / 2
	memo := make([][]int, len(nums))
	for i := 0; i < len(nums); i++ {
		memo[i] = make([]int, target+1)
	}
	var dfs func(i, target int) bool
	dfs = func(i, target int) bool {
		if i >= len(nums) {
			return false
		}
		if target == nums[i] {
			return true
		}
		if target < nums[i] {
			return false
		}
		if memo[i][target] != 0 {
			return false
		}
		ret := dfs(i+1, target-nums[i]) || dfs(i+1, target)
		if !ret {
			memo[i][target] = 1
		}
		return ret
	}
	return dfs(0, target)
}
