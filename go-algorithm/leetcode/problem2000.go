package main

import "strings"

// 2000. Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

func reversePrefix(word string, ch byte) string {
	idx := strings.IndexByte(word, ch)
	if idx == -1 {
		return word
	}
	ans := ""
	for _, v := range word[:idx+1] {
		ans = string(v) + ans
	}
	return ans + word[idx+1:]
}
