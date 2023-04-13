package main

// 476. Number Complement
// https://leetcode.com/problems/number-complement/
func findComplement(num int) int {
	ans := 0
	mul := 0
	for num > 0 {
		if num&1 == 0 {
			ans += 1 << mul
		}
		num = num >> 1
		mul++
	}
	return ans
}
