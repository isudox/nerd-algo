package main

// 34. Find First and Last Position of Element in Sorted Array
//

func searchRange(nums []int, target int) []int {
	binSearch := func(arr []int, num int) int {
		lo, hi := 0, len(arr)-1
		for lo <= hi {
			mid := (lo + hi) >> 1
			if arr[mid] == num {
				return mid
			}
			if arr[mid] < num {
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}
		return -1
	}
	pos := binSearch(nums, target)
	if pos == -1 {
		return []int{-1, -1}
	}
	l, r := pos, pos
	for l >= 0 && nums[l] == target {
		l -= 1
	}
	for r < len(nums) && nums[r] == target {
		r += 1
	}
	return []int{l + 1, r - 1}
}
