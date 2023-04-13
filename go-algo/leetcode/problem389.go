package main

// 389. Find the Difference
// https://leetcode.com/problems/find-the-difference/

func findTheDifference(s string, t string) byte {
	cntT, cntS := make(map[byte]int, 0), make(map[byte]int, 0)
	for i := 0; i < len(t); i++ {
		cntT[t[i]]++
	}
	for i := 0; i < len(s); i++ {
		cntS[s[i]]++
	}
	for k, v := range cntT {
		if v != cntS[k] {
			return k
		}
	}
	return byte(0)
}
