package main

func minSteps(n int) int {
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, n+1)
		for j := 0; j <= n; j++ {
			dp[i][j] = n
		}
	}
	dp[1][0] = 0
	dp[1][1] = 1
	ans := 0
	for i := 2; i <= n; i++ {
		ans = i
		for j := 0; j < i; j++ {
			if dp[i][j] > dp[i-j][j]+1 {
				dp[i][j] = dp[i-j][j] + 1
			}
			if dp[i][j] < ans {
				ans = dp[i][j]
			}
		}
		dp[i][i] = ans + 1
	}
	return ans
}
