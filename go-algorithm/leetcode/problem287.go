package main

// 287. Find the Duplicate Number
// https://leetcode.com/problems/find-the-duplicate-number/

func findDuplicate(nums []int) int {
	n := len(nums)
	ans := 0
	bits := 31
	for ((n - 1) >> bits) == 0 {
		bits-- // calculate the highest bit
	}
	for i := 0; i <= bits; i++ {
		x, y := 0, 0
		for j := 0; j < n; j++ {
			if (nums[j] & (1 << i)) > 0 {
				x++ // count the `1` of current bit of nums array
			}
			if j >= 1 && (j&(1<<i)) > 0 {
				y++ // count the `1` in current bit of [1, n] array
			}
		}
		if x > y {
			ans |= 1 << i // if x > y, then the current bit of duplicate num is 1
		}
	}
	return ans
}
