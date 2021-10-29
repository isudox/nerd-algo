package leetcode

import (
	"fmt"
	"sort"
)

// 15. 3Sum
// https://leetcode.com/problems/3sum/

func threeSum(nums []int) [][]int {
	n := len(nums)
	if n < 3 {
		return [][]int{}
	}
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	var store = map[string]bool{}
	getKey := func(x, y, z int) string {
		return fmt.Sprintf("%d-%d-%d", x, y, z)
	}
	twoSum := func(pos int, target int) [][]int {
		var ret [][]int
		var memo = map[int]bool{}
		for i := pos; i < n; i++ {
			if memo[target-nums[i]] == true {
				ret = append(ret, []int{target - nums[i], nums[i]})
			} else {
				memo[nums[i]] = true
			}
		}
		return ret
	}
	var ans [][]int
	for i := 0; i < n-2; i++ {
		ret := twoSum(i+1, -nums[i])
		if len(ret) > 0 {
			for _, couple := range ret {
				key := getKey(nums[i], couple[0], couple[1])
				if store[key] == false {
					store[key] = true
					ans = append(ans, []int{nums[i], couple[0], couple[1]})
				}
			}
		}
	}
	return ans
}
