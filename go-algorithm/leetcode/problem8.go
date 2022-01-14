package main

import (
	"fmt"
	"strconv"
)

// 8. String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

const (
	MaxInt = 2147483647
	MinInt = -2147483648
)

func myAtoi(s string) int {
	ans := 0
	isNeg, foundNum := false, false
	for _, ch := range s {
		cur := fmt.Sprintf("%c", ch)
		if !foundNum && (cur > "9" || cur < "0") {
			if cur == "+" || cur == "-" {
				foundNum = true
				isNeg = cur == "-"
				continue
			} else if cur == " " {
				continue
			} else {
				break
			}
		}
		if (cur == "+" || cur == "-") && !foundNum {
			foundNum = true
			if cur == "-" {
				isNeg = true
			}
			continue
		}
		if "0" <= cur && cur <= "9" {
			if !foundNum {
				foundNum = true
			}
			val, _ := strconv.Atoi(cur)
			if isNeg {
				val = -val
			}
			if isNeg {
				if (MinInt-val)/10 > ans {
					return MinInt
				}
			} else {
				if (MaxInt-val)/10 < ans {
					return MaxInt
				}
			}
			ans = ans*10 + val
		}
		if foundNum && (cur > "9" || cur < "0") {
			break
		}
	}
	return ans
}
