package main

// 96. Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

func numTrees(n int) int {
	memo := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		memo[i] = make([]int, n+1)
	}
	var dfs func(x, y int) int
	dfs = func(x, y int) int {
		if x > y {
			return 1
		}
		if memo[x][y] > 0 {
			return memo[x][y]
		}
		ret := 0
		for i := x; i <= y; i++ {
			ret += dfs(x, i-1) * dfs(i+1, y)
		}
		memo[x][y] = ret
		return ret
	}
	return dfs(1, n)
}
