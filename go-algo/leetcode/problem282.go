package main

import (
	"strconv"
	"strings"
)

// 282. Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/
func addOperators(num string, target int) []string {
	n := len(num)
	var ans []string
	var recur func(idx int, preOperand int, curOperand int, value int, expr []string)
	recur = func(idx int, preOperand int, curOperand int, value int, expr []string) {
		if idx == n {
			if value == target && curOperand == 0 {
				ans = append(ans, strings.Join(expr[1:], ""))
			}
			return
		}
		curOperand = curOperand*10 + int(num[idx]) - '0'
		strOperand := strconv.Itoa(curOperand)
		if curOperand > 0 {
			recur(idx+1, preOperand, curOperand, value, expr)
		}
		expr = append(expr, "+", strOperand)
		recur(idx+1, curOperand, 0, value+curOperand, expr)
		expr = expr[:len(expr)-2]
		if len(expr) > 0 {
			expr = append(expr, "-", strOperand)
			recur(idx+1, -curOperand, 0, value-curOperand, expr)
			expr = expr[:len(expr)-2]
			expr = append(expr, "*", strOperand)
			recur(idx+1, curOperand*preOperand, 0, value-preOperand+(curOperand*preOperand), expr)
			expr = expr[:len(expr)-2]
		}
	}
	var expr []string
	recur(0, 0, 0, 0, expr)
	return ans
}
