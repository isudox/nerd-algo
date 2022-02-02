package main

// 438. Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

func findAnagrams(s string, p string) []int {
	ans := make([]int, 0)
	if len(s) < len(p) {
		return ans
	}
	var pattern, counter [26]int
	for i, v := range p {
		pattern[v-'a']++
		counter[s[i]-'a']++
	}
	if pattern == counter {
		ans = append(ans, 0)
	}
	for i := len(p); i < len(s); i++ {
		counter[s[i]-'a']++
		counter[s[i-len(p)]-'a']--
		if counter == pattern {
			ans = append(ans, i-len(p)+1)
		}
	}
	return ans
}
