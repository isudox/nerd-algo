package main

// 375. Guess Number Higher or Lower II
// https://leetcode.com/problems/guess-number-higher-or-lower-ii/

func getMoneyAmount(n int) int {
	memo := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		memo[i] = make([]int, n+1)
	}
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if i >= j {
			return 0
		}
		if memo[i][j] > 0 {
			return memo[i][j]
		}
		ret := 20100
		for k := i; k <= j; k++ {
			tmp := max(dfs(i, k - 1), dfs(k+1,j)) + k
			ret = min(tmp, ret)
		}
		memo[i][j] = ret
		return ret
	}
	return dfs(1, n)
}
