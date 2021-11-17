package main

import (
	"sort"
)

// 368. Largest Divisible Subset
// https://leetcode.com/problems/largest-divisible-subset/
// TODO

func largestDivisibleSubset(nums []int) []int {
	sort.Slice(nums, func(x, y int) bool {
		return nums[x] < nums[y]
	})
	n := len(nums)
	memo := make([][][]int, n)
	for i := 0; i < n; i++ {
		memo[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			memo[i][j] = make([]int, 0)
		}
	}
	maxCnt := 0
	var ans []int
	var dfs func(i, j int) []int
	dfs = func(i, j int) []int {
		if j == n-1 {
			return []int{nums[i], nums[j]}
		}
		if len(memo[i][j]) != 0 {
			return memo[i][j]
		}
		curSize := 2
		curList := make([]int, 2)
		curList = append(curList, nums[i], nums[j])
		for k := j + 1; k < n; k++ {
			if nums[k]%nums[j] == 0 {
				nextList := dfs(j, k)
				if size := len(nextList) + 1; size > curSize {
					curSize = size
					curList = append(curList[:len(curList)-1], nextList...)
				}
			}
		}
		memo[i][j] = curList
		if len(curList) > maxCnt {
			ans = curList
		}
		return curList
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if nums[j]%nums[i] == 0 {
				dfs(i, j)
			}
		}
	}
	return ans
}

//func main() {
//	arg := []int{5, 9, 18, 54, 108, 540, 90, 180, 360, 720}
//	ans := largestDivisibleSubset(arg)
//	fmt.Printf("ans: %v", ans) //[2,4,8]
//}
