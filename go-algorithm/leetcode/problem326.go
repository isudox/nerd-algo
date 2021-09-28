package leetcode

// 326. Power of Three
// https://leetcode-cn.com/problems/power-of-three/
func isPowerOfThree(n int) bool {
	if n <= 0 {
		return false
	}
	if n == 1 {
		return true
	}
	rem := n % 3
	if rem != 0 {
		return false
	}
	return isPowerOfThree(n / 3)
}
