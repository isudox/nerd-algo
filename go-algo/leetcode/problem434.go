package main

// 434. Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/
func countSegments(s string) int {
	ans := 0
	seg := ""
	for _, ch := range s {
		if ch == ' ' {
			if seg != "" {
				ans++
			}
			seg = ""
		} else {
			seg += string(ch)
		}
	}
	if seg != "" {
		ans++
	}
	return ans
}
