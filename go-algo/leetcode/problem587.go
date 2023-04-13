package main

import "sort"

// 587. Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

func outerTrees(trees [][]int) [][]int {
	n := len(trees)
	if n < 4 {
		return trees
	}
	sort.Slice(trees, func(i, j int) bool {
		a, b := trees[i], trees[j]
		return a[0] < b[0] || a[0] == b[0] && a[1] < b[1]
	})
	hull := []int{0}
	used := make([]bool, n)
	for i := 1; i < n; i++ {
		for len(hull) > 1 && cross(trees[hull[len(hull)-2]], trees[hull[len(hull)-1]], trees[i]) < 0 {
			used[hull[len(hull)-1]] = false
			hull = hull[:len(hull)-1]
		}
		used[i] = true
		hull = append(hull, i)
	}
	m := len(hull)
	for i := n - 2; i >= 0; i-- {
		if !used[i] {
			for len(hull) > m && cross(trees[hull[len(hull)-2]], trees[hull[len(hull)-1]], trees[i]) < 0 {
				used[hull[len(hull)-1]] = false
				hull = hull[:len(hull)-1]
			}
			used[i] = true
			hull = append(hull, i)
		}
	}
	hull = hull[:len(hull)-1]
	ans := make([][]int, len(hull))
	for i, idx := range hull {
		ans[i] = trees[idx]
	}
	return ans
}

func cross(p, q, r []int) int {
	return (q[0]-p[0])*(r[1]-q[1]) - (q[1]-p[1])*(r[0]-q[0])
}
