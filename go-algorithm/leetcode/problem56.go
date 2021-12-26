package main

import "sort"

// 56. Merge Intervals
// https://leetcode.com/problems/merge-intervals/

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	isOverlap := func(a, b []int) bool {
		return a[1] >= b[0]
	}
	mergeInterval := func(a, b []int) []int {
		ret := make([]int, 2)
		if a[0] < b[0] {
			ret[0] = a[0]
		} else {
			ret[0] = b[0]
		}
		if a[1] > b[1] {
			ret[1] = a[1]
		} else {
			ret[1] = b[1]
		}
		return ret
	}
	mark := make([]bool, len(intervals))
	for i := 0; i < len(mark); i++ {
		mark[i] = true
	}
	for i := 0; i < len(intervals)-1; i++ {
		if isOverlap(intervals[i], intervals[i+1]) {
			ret := mergeInterval(intervals[i], intervals[i+1])
			intervals[i+1] = ret
			mark[i] = false
			mark[i+1] = true
		} else {
			mark[i] = true
			mark[i+1] = true
		}
	}
	ans := make([][]int, 0)
	for i := 0; i < len(intervals); i++ {
		if mark[i] {
			ans = append(ans, intervals[i])
		}
	}
	return ans
}
