package leetcode

import "strconv"

func fizzBuzz(n int) []string {
	var ans []string
	for i := 1; i <= n; i++ {
		if i%15 == 0 {
			ans = append(ans, "FizzBuzz")
		} else if i%3 == 0 {
			ans = append(ans, "Fizz")
		} else if i%5 == 0 {
			ans = append(ans, "Buzz")
		} else {
			ans = append(ans, strconv.Itoa(i))
		}
	}
	return ans
}
