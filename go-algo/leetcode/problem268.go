package main

// 268. Missing Number
// https://leetcode.com/problems/missing-number/

func missingNumber(nums []int) int {
	n := len(nums)
	sum := (n + 1) * n / 2
	for _, num := range nums {
		sum -= num
	}
	return sum
}
