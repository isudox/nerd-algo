package main

//
//

func isPerfectSquare(num int) bool {
	if num < 0 {
		return false
	}
	l, r := 0, num
	for l < r {
		mid := l + (r-l)/2
		cur := mid * mid
		if cur == num {
			return true
		}
		if cur < num {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return l*l == num
}
