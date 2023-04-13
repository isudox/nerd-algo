package main

//

func minStartValue(nums []int) int {
	ans, sum := 1, 1
	for _, num := range nums {
		sum += num
		if sum < 1 {
			ans += 1 - sum
			sum = 1
		}
	}
	return ans
}
