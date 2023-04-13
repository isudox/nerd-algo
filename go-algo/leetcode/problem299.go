package main

import "fmt"

// 299. Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

func getHint(secret string, guess string) string {
	n := len(secret)
	bulls, cows := 0, 0
	cnt1, cnt2 := make([]int, 10), make([]int, 10)
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
		cnt1[secret[i]-'0']++
		cnt2[guess[i]-'0']++
	}
	for i := 0; i < 10; i++ {
		cows += min(cnt1[i], cnt2[i])
	}
	cows -= bulls
	return fmt.Sprintf("%dA%dB", bulls, cows)
}
