package main

import "unicode"

// 500. Keyboard Row
// https://leetcode.com/problems/keyboard-row/

func findWords2(words []string) []string {
	rowIndex := "12210111011122000010020202"
	ans := make([]string, 0)
next:
	for _, word := range words {
		idx := rowIndex[unicode.ToLower(rune(word[0]))-'a']
		for i := 1; i < len(word); i++ {
			if rowIndex[unicode.ToLower(rune(word[i])-'a')] != idx {
				continue next
			}
		}
		ans = append(ans, word)
	}
	return ans
}
