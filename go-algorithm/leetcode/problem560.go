package main

// 560. Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

func subarraySum(nums []int, k int) int {
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	store := make(map[int]int, 0)
	store[0] = 1
	ans := 0
	for i := 0; i < len(nums); i++ {
		ans += store[nums[i]-k]
		store[nums[i]]++
	}
	return ans
}
