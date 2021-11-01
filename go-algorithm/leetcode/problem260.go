package main

// 260. Single Number III
// https://leetcode.com/problems/single-number-iii/

func singleNumber(nums []int) []int {
	counter := make(map[int]int)
	ans := make([]int, 0)
	for _, num := range nums {
		counter[num]++
	}
	for num, cnt := range counter {
		if cnt == 1 {
			ans = append(ans, num)
		}
	}
	return ans
}
