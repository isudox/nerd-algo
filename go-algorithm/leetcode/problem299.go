package main

import "fmt"

// 299. Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

func getHint(secret string, guess string) string {
	n := len(secret)
	bulls, cows := 0, 0
	counter1 := make([]int, 10)
	counter2 := make([]int, 10)
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	for i := 0; i < n; i++ {
		if secret[i] == guess[i] {
			bulls++
		}
		counter1[secret[i]-'0']++
		counter2[guess[i]-'0']++
	}
	for i := 0; i < 10; i++ {
		cows += min(counter1[i], counter2[i])
	}
	cows -= bulls
	return fmt.Sprintf("%dA%dB", bulls, cows)
}
