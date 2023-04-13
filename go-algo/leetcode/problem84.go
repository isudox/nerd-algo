package main

// 84. Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

func largestRectangleArea(heights []int) int {
	ans := 0
	stack := make([]int, 0)
	for i := 0; i < len(heights) || len(stack) > 0; {
		if len(stack) == 0 || (i < len(heights) && heights[stack[len(stack)-1]] <= heights[i]) {
			stack = append(stack, i)
			i++
		} else {
			top := stack[len(stack)-1]
			stack = stack[0 : len(stack)-1]
			area := 0
			if len(stack) == 0 {
				area = heights[top] * i
			} else {
				area = heights[top] * (i - stack[len(stack)-1] - 1)
			}
			if area > ans {
				ans = area
			}
		}
	}
	return ans
}
