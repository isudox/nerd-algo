package leetcode

import "math"

// 29. Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

func divide(dividend int, divisor int) int {
	if dividend == math.MinInt32 && divisor == -1 {
		return math.MaxInt32
	}
	if dividend < 0 && divisor < 0 {
		return divide(-dividend, -divisor)
	}
	if dividend < 0 {
		return -divide(-dividend, divisor)
	}
	if divisor < 0 {
		return -divide(dividend, -divisor)
	}
	if dividend < divisor {
		return 0
	}
	ans := 1
	dividend -= divisor
	y := divisor
	for dividend >= y {
		dividend -= y
		y += y
		ans += ans
	}
	return ans + divide(dividend, divisor)
}
