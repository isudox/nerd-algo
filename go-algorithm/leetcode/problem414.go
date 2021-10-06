package leetcode

// 414. Third Maximum Number
// https://leetcode.com/problems/third-maximum-number/
func thirdMax(nums []int) int {
	var a, b, c *int
	for _, num := range nums {
		cur := num
		if a == nil || num > *a {
			a, b, c = &cur, a, b
		} else if *a > num && (b == nil || *b < num) {
			b, c = &cur, b
		} else if b != nil && *b > num && (c == nil || *c < num) {
			c = &cur
		}
	}
	if c == nil {
		return *a
	}
	return *c
}
