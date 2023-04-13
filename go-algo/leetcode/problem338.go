package main

// 338. Counting Bits
// https://leetcode.com/problems/counting-bits/

func countBits(n int) []int {
	ans := []int{0}
	for len(ans) < n+1 {
		m := len(ans)
		for i := 0; i < m; i++ {
			ans = append(ans, ans[i]+1)
			if len(ans) == n+1 {
				break
			}
		}
	}
	return ans
}
