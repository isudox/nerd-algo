package main

// 152. Maximum Product Subarray
// https://leetcode.com/problems/maximum-product-subarray/

func maxProduct(nums []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	ans := nums[0]
	dp1, dp2 := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		tmp1, tmp2 := dp1, dp2
		dp1 = max(tmp1*nums[i], max(nums[i], tmp2*nums[i]))
		dp2 = min(tmp2*nums[i], min(nums[i], tmp1*nums[i]))
		ans = max(ans, dp1)
	}
	return ans
}
