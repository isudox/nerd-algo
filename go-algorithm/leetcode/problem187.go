package main

import "math"

// 187. Repeated DNA Sequences
// https://leetcode.com/problems/repeated-dna-sequences/
func findRepeatedDnaSequences(s string) []string {
	mapper := make(map[byte]int)
	mapper['A'] = 0
	mapper['C'] = 1
	mapper['G'] = 2
	mapper['T'] = 3
	base := int(math.Pow(4, 9))
	encode := func(x int, preCode int) int {
		return (preCode-mapper[s[x-10]]*base)*4 + mapper[s[x]]
	}
	ans := make([]string, 0)
	if len(s) < 10 {
		return ans
	}
	seen := make(map[int]bool)
	memo := make(map[int]int)
	code := 0
	for i := 0; i < 10; i++ {
		code = code*4 + mapper[s[i]]
	}
	seen[code] = true
	for i := 10; i < len(s); i++ {
		code = encode(i, code)
		if seen[code] {
			if memo[code] == 0 {
				memo[code] = i
			}
		} else {
			seen[code] = true
		}
	}
	for _, i := range memo {
		ans = append(ans, s[i-9:i+1])
	}
	return ans
}
