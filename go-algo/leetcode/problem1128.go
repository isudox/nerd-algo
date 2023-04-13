package main

// 1128.

func longestSubsequence(arr []int, difference int) int {
	n := len(arr)
	memo := make([]int, n)
	posMap := make(map[int]int)
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	var dfs func(i int) int
	dfs = func(i int) int {
		if memo[i] != 0 {
			return memo[i]
		}
		ret := 0
		if nextPos := posMap[arr[i]+difference]; nextPos > 0 {
			ret = dfs(nextPos) + 1
		} else {
			ret = 1
		}
		memo[i] = ret
		return ret
	}
	ans := 0
	for i := n - 1; i >= 0; i-- {
		ans = max(ans, dfs(i))
		posMap[arr[i]] = i
	}
	return ans
}
