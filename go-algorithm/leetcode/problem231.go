package main

// 231. Power of Two
// https://leetcode.com/problems/power-of-two/

func isPowerOfTwo(n int) bool {
	if n <= 0 {
		return false
	}
	if n == 1 {
		return true
	}
	for n > 1 {
		if n%2 != 0 {
			return false
		}
		n /= 2
	}
	return true
}
