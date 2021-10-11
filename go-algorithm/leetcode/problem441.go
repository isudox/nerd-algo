package leetcode

// 441. Arranging Coins
// https://leetcode.com/problems/arranging-coins/
func arrangeCoins(n int) int {
	ans, sum := 1, 0
	for ; sum < n; ans++ {
		sum += ans
	}
	if sum == n {
		return ans - 1
	} else {
		return ans - 2
	}
}
