package main

// 136. Single Number
// https://leetcode.com/problems/single-number/

func singleNumber(nums []int) int {
	ans := 0
	for _, num := range nums {
		ans = ans ^ num
	}
	return ans
}
