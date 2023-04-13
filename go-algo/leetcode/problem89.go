package main

// 89. Gray Code
// https://leetcode.com/problems/gray-code/

func grayCode(n int) []int {
	ans := make([]int, 0)
	size := 1 << n
	for i := 0; i < size; i++ {
		ans = append(ans, i^(i>>1))
	}
	return ans
}
