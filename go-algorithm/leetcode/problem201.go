package main

// 201. Bitwise AND of Numbers Range
// https://leetcode.com/problems/bitwise-and-of-numbers-range/

func rangeBitwiseAnd(left int, right int) int {
	ans := left
	for i := left; i <= right; i++ {
		ans = ans & i
	}
	return ans
}
