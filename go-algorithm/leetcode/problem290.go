package main

import "strings"

// 290. Word Pattern
// https://leetcode.com/problems/word-pattern/

func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")
	if len(pattern) != len(words) {
		return false
	}
	dict := make(map[uint8]string, 0)
	revertDict := make(map[string]uint8, 0)
	for i := 0; i < len(pattern); i++ {
		ch, word := pattern[i], words[i]
		if v, ok := dict[ch]; !ok {
			if _, ok := revertDict[word]; ok {
				return false
			}
			dict[ch] = word
			revertDict[word] = ch
		} else {
			if word != v {
				return false
			}
		}
	}
	return true
}
