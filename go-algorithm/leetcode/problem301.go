package leetcode

// 301. Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

func removeInvalidParentheses(s string) []string {
	minDelCnt := len(s)
	candidates := make(map[string]bool)
	var helper func(i int, leftCnt, rightCnt, delCnt int, expr string)
	helper = func(i int, leftCnt, rightCnt, delCnt int, expr string) {
		if i == len(s) {
			if leftCnt == rightCnt {
				if delCnt < minDelCnt {
					minDelCnt = delCnt
					candidates = make(map[string]bool)
					candidates[expr] = true
				} else if delCnt == minDelCnt {
					candidates[expr] = true
				}
			}
		} else if s[i] != '(' && s[i] != ')' {
			helper(i+1, leftCnt, rightCnt, delCnt, expr+string(s[i]))
		} else {
			helper(i+1, leftCnt, rightCnt, delCnt+1, expr)
			if s[i] == '(' {
				helper(i+1, leftCnt+1, rightCnt, delCnt, expr+"(")
			} else if leftCnt > rightCnt {
				helper(i+1, leftCnt, rightCnt+1, delCnt, expr+")")
			}
		}
	}
	helper(0, 0, 0, 0, "")
	var ans []string
	for expr := range candidates {
		ans = append(ans, expr)
	}
	return ans
}
