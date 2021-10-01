package leetcode

func findMinMoves(machines []int) (ans int) {
	var abs func(x int) int
	abs = func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	sum, n := 0, len(machines)
	for _, v := range machines {
		sum += v
	}
	if sum%n > 0 {
		return -1
	}
	avg := sum / n
	preSum := 0
	for _, num := range machines {
		num -= avg
		preSum += num
		ans = max(ans, max(abs(preSum), num))
	}
	return
}
