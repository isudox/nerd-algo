package main

import "sort"

// 973. K Closest Points to Origin
// https://leetcode.com/problems/k-closest-points-to-origin/

func kClosest(points [][]int, k int) [][]int {
	getDist := func(p []int) int {
		return p[0]*p[0] + p[1]*p[1]
	}
	sort.Slice(points, func(i, j int) bool {
		return getDist(points[i]) < getDist(points[j])
	})
	ans := make([][]int, k)
	for i := 0; i < k; i++ {
		ans[i] = points[i]
	}
	return ans
}
