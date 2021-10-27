package leetcode

// 75. Sort Colors
// https://leetcode.com/problems/sort-colors/

func sortColors(nums []int) {
	i, l, r := 0, 0, len(nums)-1
	for i <= r {
		if nums[i] == 0 {
			nums[i], nums[l] = nums[l], nums[i]
			l++
			i++
		} else if nums[i] == 2 {
			nums[i], nums[r] = nums[r], nums[i]
			r--
		} else {
			i++
		}
	}
}
