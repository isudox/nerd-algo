package main

import "strings"

// 482. License Key Formatting
// https://leetcode.com/problems/license-key-formatting/
func licenseKeyFormatting(s string, k int) string {
	var chars []string
	for _, ch := range s {
		if ch != '-' {
			chars = append(chars, strings.ToUpper(string(ch)))
		}
	}
	n := len(chars)
	if n == 0 {
		return ""
	}
	groups := n / k
	first := n % k
	if first > 0 {
		groups++
	} else {
		first = k
	}
	ans := strings.Join(chars[:first], "")
	for i := first; i < n; i += k {
		ans += "-" + strings.Join(chars[i:i+k], "")
	}
	return ans
}
