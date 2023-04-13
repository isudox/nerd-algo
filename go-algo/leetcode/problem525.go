package main

// 525. Contiguous Array
// https://leetcode.com/problems/contiguous-array/

func findMaxLength(nums []int) int {
	if nums[0] == 0 {
		nums[0] = -1
	}
	ans := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] == 1 {
			nums[i] = nums[i-1] + 1
		} else {
			nums[i] = nums[i-1] - 1
		}
		if nums[i] == 0 && i > ans {
			ans = i + 1
		}
	}
	store := make(map[int]int, 0)
	for i := 0; i < len(nums); i++ {
		if val, ok := store[nums[i]]; !ok {
			store[nums[i]] = i
		} else if i-val > ans {
			ans = i - val
		}
	}
	return ans
}
