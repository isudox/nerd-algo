package leetcode

// 496. Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

func nextGreaterElement1(nums1 []int, nums2 []int) []int {
	m, n := len(nums1), len(nums2)
	memo := make(map[int]int)
	var stack []int
	for i := 0; i < n; i++ {
		for len(stack) != 0 && stack[len(stack)-1] < nums2[i] {
			memo[stack[len(stack)-1]] = nums2[i]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, nums2[i])
	}
	ans := make([]int, m)
	for i := 0; i < m; i++ {
		if memo[nums1[i]] != 0 {
			ans[i] = memo[nums1[i]]
		} else {
			ans[i] = -1
		}
	}
	return ans
}
