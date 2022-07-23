package main

// 315. Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

func countSmaller(nums []int) []int {
	binSearch := func(arr []int, x int) int {
		if len(arr) == 0 {
			return 0
		}
		if x <= arr[0] {
			return 0
		}
		if x > arr[len(arr)-1] {
			return len(arr)
		}
		lo, hi, mid := 0, len(arr)-1, 0
		for lo < hi {
			mid = (lo + hi + 1) >> 1
			if arr[mid] >= x {
				hi = mid - 1
			} else {
				lo = mid
			}
		}
		return lo + 1
	}
	ans := make([]int, len(nums))
	store := []int{10000000}
	for i := len(nums) - 1; i >= 0; i-- {
		pos := binSearch(store, nums[i])
		ans[i] = pos
		store = append(store[:pos+1], store[pos:]...)
		store[pos] = nums[i]
	}
	return ans
}
