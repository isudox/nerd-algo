package leetcode

// 583. Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/
func minDistance(word1 string, word2 string) int {
	var min func(x, y int) int
	min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	m, n := len(word1), len(word2)
	dp := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		dp[i] = make([]int, n+1)
		dp[i][0] = i
	}
	for i := 0; i <= n; i++ {
		dp[0][i] = i
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				dp[i][j] = min(min(dp[i-1][j]+1, dp[i][j-1]+1), dp[i-1][j-1]+2)
			}
		}
	}
	return dp[m][n]
}
