package main

// 13. Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

func romanToInt(s string) int {
	mapper := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	ans := 0
	ss := []rune(s)
	for i := 0; i < len(ss); i++ {
		ans += mapper[ss[i]]
		if i > 0 && mapper[ss[i]] > mapper[ss[i-1]] {
			ans -= mapper[ss[i-1]] * 2
		}
	}
	return ans
}
