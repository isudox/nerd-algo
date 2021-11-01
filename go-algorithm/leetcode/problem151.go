package main

import "strings"

// 151. Reverse Words in a String
// https://leetcode.com/problems/reverse-words-in-a-string/

func reverseWords(s string) string {
	arr := strings.Split(s, " ")
	var store []string
	for _, word := range arr {
		if word != "" {
			store = append(store, word)
		}
	}
	ans := ""
	for i := len(store) - 1; i >= 0; i-- {
		ans += store[i]
		if i > 0 {
			ans += " "
		}
	}
	return ans
}
