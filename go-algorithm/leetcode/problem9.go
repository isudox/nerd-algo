package main

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	var digits []int
	for x > 0 {
		y := x % 10
		x = x / 10
		digits = append(digits, y)
	}
	i := 0
	j := len(digits)
	for i < j {
		if digits[i] != digits[j] {
			return false
		}
		i++
		j--
	}
	return true
}
