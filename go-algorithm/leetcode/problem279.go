package leetcode

func numSquares(n int) int {
	memo := make(map[int]int)
	var helper func(x int) int
	helper = func(x int) int {
		if x == 0 {
			return 0
		}
		if memo[x] != 0 {
			return memo[x]
		}
		ret := x
		for i := 1; i*i <= x; i++ {
			if cur := helper(x-i*i) + 1; cur < ret {
				ret = cur
			}
		}
		memo[x] = ret
		return ret
	}
	return helper(n)
}
