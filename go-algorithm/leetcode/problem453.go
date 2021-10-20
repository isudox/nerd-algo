package leetcode

import "math"

func minMoves(nums []int) int {
	sum, min := 0, math.MaxInt32
	for _, num := range nums {
		if num < min {
			min = num
		}
		sum += num
	}
	return sum - min * len(nums)
}
