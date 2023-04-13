package main

import "strconv"

// 38. Count and Say
// https://leetcode.com/problems/count-and-say/

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}
	var helper func(x string) string
	helper = func(x string) string {
		ret, cnt := "", 1
		for i := 1; i < len(x); i++ {
			if x[i] == x[i-1] {
				cnt++
			} else {
				ret += strconv.Itoa(cnt) + string(x[i-1])
				cnt = 1
			}
		}
		ret += strconv.Itoa(cnt) + string(x[len(x)-1])
		return ret
	}
	ans := "1"
	for i := 1; i < n; i++ {
		ans = helper(ans)
	}
	return ans
}
