package main

// 392. Is Subsequence
// https://leetcode.com/problems/is-subsequence/

func isSubsequence(s string, t string) bool {
	m, n := len(s), len(t)
	if m > n {
		return false
	}
	i, j := 0, 0
	for i < m && j < n {
		if s[i] == t[j] {
			i++
			j++
		} else {
			j++
		}
	}
	return i == m
}
