package main

// 260. Single Number III
// https://leetcode.com/problems/single-number-iii/

func singleNumber3(nums []int) []int {
	counter := make(map[int]int)
	for _, num := range nums {
		if _, ok := counter[num]; ok {
			delete(counter, num)
		} else {
			counter[num]++
		}
	}
	ans := make([]int, 0)
	for num := range counter {
		ans = append(ans, num)
	}
	return ans
}
