package main

// 374. Guess Number Higher or Lower
// https://leetcode.com/problems/guess-number-higher-or-lower/

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */
func guessNumber(n int) int {
	l, r, mid := 1, n, 1
	for l <= r {
		mid = l + (r-l)/2
		ret := guess(mid)
		if ret == 0 {
			return mid
		}
		if ret == -1 {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return mid
}

func guess(num int) int {
	return 0
}
