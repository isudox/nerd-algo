package main

// 442. Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/
func findDuplicates(nums []int) []int {
	memo := make(map[int]bool)
	var ans []int
	for _, num := range nums {
		if memo[num] {
			ans = append(ans, num)
		} else {
			memo[num] = true
		}
	}
	return ans
}
func findDuplicates2(nums []int) []int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	var ans []int
	for _, num := range nums {
		idx := abs(num) - 1
		if nums[idx] < 0 {
			ans = append(ans, abs(idx+1))
		}
		nums[idx] = -nums[idx]
	}
	return ans
}
