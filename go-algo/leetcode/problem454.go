package main

// 454. 4Sum II
// https://leetcode.com/problems/4sum-ii/

func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	store := make(map[int]int, 0)
	for i := 0; i < len(nums1); i++ {
		for j := 0; j < len(nums2); j++ {
			target := -nums1[i] - nums2[j]
			store[target]++
		}
	}
	ans := 0
	for i := 0; i < len(nums3); i++ {
		for j := 0; j < len(nums4); j++ {
			ans += store[nums3[i]+nums4[j]]
		}
	}
	return ans
}
