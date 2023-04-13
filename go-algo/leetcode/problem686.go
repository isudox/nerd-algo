package main

import "strings"

// 686. Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

func repeatedStringMatch(a string, b string) int {
	ans := 1
	str := a
	for len(str) < 2*len(a)+len(b) {
		if strings.Contains(str, b) {
			return ans
		}
		str += a
		ans++
	}
	return -1
}
