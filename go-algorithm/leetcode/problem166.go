package main

import "strconv"

// 166. Fraction to Recurring Decimal
// https://leetcode.com/problems/fraction-to-recurring-decimal/
func fractionToDecimal(numerator int, denominator int) string {
	if numerator < 0 && denominator > 0 {
		return "-" + fractionToDecimal(-numerator, denominator)
	}
	if numerator > 0 && denominator < 0 {
		return "-" + fractionToDecimal(numerator, -denominator)
	}
	ans, rem := strconv.Itoa(numerator/denominator), ""
	numerator = (numerator % denominator) * 10
	seen := make(map[int]bool)
	for numerator != 0 {
		if seen[numerator] {
			v := findRepeating(numerator, denominator)
			rem = rem[:len(rem)-len(v)] + "(" + rem[len(rem)-len(v):] + ")"
			break
		}
		res := strconv.Itoa(numerator / denominator)
		seen[numerator] = true
		rem += res
		numerator = (numerator % denominator) * 10
	}
	if len(rem) > 0 {
		return ans + "." + rem
	}
	return ans
}

func findRepeating(x, y int) string {
	res := ""
	z := x
	for true {
		res += strconv.Itoa(x / y)
		x = (x % y) * 10
		if x == z {
			break
		}
	}
	return res
}
