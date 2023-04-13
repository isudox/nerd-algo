package main

// 852. Peak Index in a Mountain Array
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

func peakIndexInMountainArray(arr []int) int {
	i, j := 0, len(arr)-1
	for i < j {
		mid := i + (j-i)/2
		if arr[mid] > arr[mid+1] && arr[mid] > arr[mid-1] {
			return mid
		}
		if arr[mid] < arr[mid-1] {
			j = mid
		} else {
			i = mid + 1
		}
	}
	return i
}
