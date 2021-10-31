package leetcode

/**
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
*/
func findPeakElement(nums []int) int {
	i, j := 0, len(nums)-1
	for i < j {
		mid := i + (j-i)/2
		if nums[mid] > nums[mid+1] {
			j = mid
		} else {
			i = mid + 1
		}
	}
	return i
}
