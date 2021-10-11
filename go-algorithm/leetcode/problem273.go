package leetcode

import "strings"

// 273. Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/
func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}
	ans := ""
	words0 := []string{"", "Thousand", "Million", "Billion"}
	words1 := []string{"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
		"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"}
	words2 := []string{"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"}
	for i := 0; num > 0; i++ {
		rem := num % 1000
		num = num / 1000
		if rem == 0 {
			continue
		}
		cur := ""
		h := rem / 100
		if h > 0 {
			cur += words1[h] + " Hundred "
		}
		rem = rem % 100
		if 0 < rem && rem < 20 {
			cur += words1[rem] + " "
		} else if rem >= 20 {
			t := rem / 10
			cur += words2[t] + " "
			rem = rem % 10
			cur += words1[rem] + " "
		}
		ans = cur + " " + words0[i] + " " + ans
	}
	strs := strings.Split(ans, " ")
	ans = ""
	for _, s := range strs {
		if s != "" {
			ans += s + " "
		}
	}
	return ans[:len(ans)-1]
}
