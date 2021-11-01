package main

// 1044. Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

func longestDupSubstring(s string) string {
	n := len(s)
	check := func(len int) (bool, string) {
		seen := make(map[string]bool)
		for i := 0; i < n-len+1; i++ {
			subStr := s[i : i+len]
			if seen[subStr] {
				return true, subStr
			}
			seen[subStr] = true
		}
		return false, ""
	}
	i, j := 1, n
	ans := ""
	for i < j {
		mid := (i + j) / 2
		if ok, ret := check(mid); ok {
			ans = ret
			i = mid + 1
		} else {
			j = mid
		}
	}
	return ans
}
