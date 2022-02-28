package main

import "fmt"

// 228. Summary Ranges
// https://leetcode.com/problems/summary-ranges/

func summaryRanges(nums []int) []string {
	ans := make([]string, 0)
	if len(nums) == 0 {
		return ans
	}
	var start int
	var end int
	for i, num := range nums {
		if i == 0 {
			start = nums[i]
			end = nums[i]
			continue
		}
		if num == nums[i-1]+1 {
			end = num
			continue
		}
		var seg string
		if start == end {
			seg = fmt.Sprintf("%d", start)
		} else {
			seg = fmt.Sprintf("%d->%d", start, end)
		}
		ans = append(ans, seg)
		start = num
		end = num
	}
	var seg string
	if start == end {
		seg = fmt.Sprintf("%d", start)
	} else {
		seg = fmt.Sprintf("%d->%d", start, end)
	}
	ans = append(ans, seg)
	return ans
}
