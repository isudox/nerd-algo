package main

// 575. Distribute Candies
// https://leetcode.com/problems/distribute-candies/

func distributeCandies(candyType []int) int {
	seen := make(map[int]bool)
	types := 0
	for _, ct := range candyType {
		if !seen[ct] {
			types++
			seen[ct] = true
		}
	}
	if n := len(candyType) / 2; n < types {
		return n
	}
	return types
}
