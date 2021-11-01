package main

import "sort"

// 698. Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
func canPartitionKSubsets(nums []int, k int) bool {
	sum := 0
	choices := make(map[int]int)
	sort.Ints(nums)
	for _, num := range nums {
		sum += num
		choices[num] += 1
	}
	if sum%k != 0 {
		return false
	}
	var helper func(target int) bool
	helper = func(target int) bool {
		if target == 0 {
			return true
		}
		if choices[target] > 0 {
			choices[target] -= 1
			return true
		}
		for i := len(nums) - 1; i >= 0; i-- {
			num := nums[i]
			if choices[num] == 0 || num > target {
				continue
			}
			choices[num] -= 1
			found := helper(target - num)
			if found {
				return true
			}
			choices[num] += 1
		}
		return false
	}
	avg := sum / k
	for i := len(nums) - 1; i >= 0; i-- {
		if choices[nums[i]] > 0 {
			choices[nums[i]] -= 1
			if !helper(avg - nums[i]) {
				return false
			}
		}
	}
	return true
}
