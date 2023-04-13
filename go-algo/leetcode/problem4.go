package main

// 4. median of two sorted arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	i, j, m, n := 0, 0, len(nums1), len(nums2)
	merged := make([]int, 0)
	for i < m && j < n {
		if nums1[i] <= nums2[j] {
			merged = append(merged, nums1[i])
			i++
		} else {
			merged = append(merged, nums2[j])
			j++
		}
	}
	if i < m {
		merged = append(merged, nums1[i:]...)
	}
	if j < n {
		merged = append(merged, nums2[j:]...)
	}
	if (m+n)%2 == 1 {
		return float64(merged[(m+n)/2])
	}
	mid0, mid1 := (m+n)/2-1, (m+n)/2
	return float64(merged[mid0]+merged[mid1]) / 2
}
