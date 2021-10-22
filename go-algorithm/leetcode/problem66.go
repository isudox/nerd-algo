package leetcode

// 66. Plus One
// https://leetcode.com/problems/plus-one/
func plusOne(digits []int) []int {
	n := len(digits)
	carry := 1
	for i := n - 1; carry == 1 && i >= 0; i-- {
		digits[i] += carry
		if digits[i] > 9 {
			digits[i] = digits[i] % 10
		} else {
			carry = 0
		}
	}
	if carry == 1 {
		digits = append(digits[0:1], digits[0:]...)
		digits[0] = 1
	}
	return digits
}
