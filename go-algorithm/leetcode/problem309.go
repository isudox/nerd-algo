package leetcode

func maxProfit(prices []int) int {
	n := len(prices)
	if n == 1 {
		return 0
	}
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	memo := make([][3]int, n)
	// state: 0, none; 1: hold stocks; 2: sold stocks last day.
	var dfs func(i int, state int) int
	dfs = func(i int, state int) int {
		if i == len(prices) {
			return 0
		}
		if memo[i][state] != 0 {
			return memo[i][state]
		}
		ret := 0
		if state == 0 {
			// buy it.
			ret = max(ret, -prices[i]+dfs(i+1, 1))
			// skip it.
			ret = max(ret, dfs(i+1, 0))
		}
		if state == 1 {
			// sell it.
			ret = max(ret, prices[i]+dfs(i+1, 2))
			// skip it.
			ret = max(ret, dfs(i+1, 1))
		}
		if state == 2 {
			// skip it.
			ret = max(ret, dfs(i+1, 0))
		}
		memo[i][state] = ret
		return ret
	}
	return dfs(0, 0)
}
