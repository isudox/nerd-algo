package leetcode

// 223. Rectangle Area
// https://leetcode.com/problems/rectangle-area/
func computeArea(ax1 int, ay1 int, ax2 int, ay2 int, bx1 int, by1 int, bx2 int, by2 int) int {
	var min func(x, y int) int
	min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	var max func(x, y int) int
	max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	area := (ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)
	x1 := max(ax1, bx1)
	y1 := max(ay1, by1)
	x2 := min(ax2, bx2)
	y2 := min(ay2, by2)
	if x1 < x2 && y1 < y2 {
		return area - (x2-x1)*(y2-y1)
	}
	return area
}
