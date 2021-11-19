package main

// 461. Hamming Distance
// https://leetcode.com/problems/hamming-distance/

func hammingDistance(x int, y int) int {
	z := x ^ y
	ans := 0
	for z > 0 {
		if bit := z & 1; bit == 1 {
			ans++
		}
		z = z >> 1
	}
	return ans
}
