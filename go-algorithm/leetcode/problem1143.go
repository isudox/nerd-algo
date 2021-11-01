package main

// 1143. Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/
func longestCommonSubsequence(text1 string, text2 string) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	m, n := len(text1), len(text2)
	var dp = make([][]int, m+1)
	for i := 0; i <= m; i++ {
		dp[i] = make([]int, n+1)
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[m][n]
}
func longestCommonSubsequence2(text1 string, text2 string) int {
	m, n := len(text1), len(text2)
	var memo = make([][]int, m)
	for i := 0; i < m; i++ {
		memo[i] = make([]int, n)
	}
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if i == m || j == n {
			return 0
		}
		if memo[i][j] != 0 {
			return memo[i][j]
		}
		ret := 0
		if text1[i] == text2[j] {
			ret = dfs(i+1, j+1) + 1
		}
		ret = max(ret, dfs(i, j+1))
		ret = max(ret, dfs(i+1, j))
		memo[i][j] = ret
		return ret
	}
	return dfs(0, 0)
}
