package main

// 739. Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	ans := make([]int, n)
	var stack []int
	for i := 0; i < n; i++ {
		t := temperatures[i]
		for len(stack) > 0 && t > temperatures[stack[len(stack)-1]] {
			prevIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[prevIdx] = i - prevIdx
		}
		stack = append(stack, i)
	}
	return ans
}
