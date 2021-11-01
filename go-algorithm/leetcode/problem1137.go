package main

// 1137. N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/
func tribonacci(n int) int {
	memo := make(map[int]int)
	return recur(n, memo)
}
func recur(n int, memo map[int]int) int {
	if n == 0 {
		return 0
	}
	if n == 1 || n == 2 {
		return 1
	}
	if memo[n] != 0 {
		return memo[n]
	}
	memo[n] = recur(n-3, memo) + recur(n-2, memo) + recur(n-1, memo)
	return memo[n]
}
