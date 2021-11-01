package main

func longestPalindrome(s string) string {
	n := len(s)
	maxLen := 0
	ans := ""
	for i := 0; i < n; i++ {
		oddStr := expand(s, i, i)
		evenStr := expand(s, i, i+1)
		if len(oddStr) > maxLen {
			ans = oddStr
			maxLen = len(oddStr)
		}
		if len(evenStr) > maxLen {
			ans = evenStr
			maxLen = len(evenStr)
		}
	}
	return ans
}

func expand(s string, left int, right int) string {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left--
		right++
	}
	return s[left+1 : right]
}
