package leetcode

// 240. Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

func searchMatrix(matrix [][]int, target int) bool {
	var helper func(x0, y0, x1, y1 int) bool
	helper = func(x0, y0, x1, y1 int) bool {
		if x0 > x1 || y0 > y1 {
			return false
		}
		if target < matrix[x0][y0] || target > matrix[x1][y1] {
			return false
		}
		if target == matrix[x0][y0] || target == matrix[x1][y1] {
			return true
		}
		midX, midY := x0+(x1-x0)/2, y0+(y1-y0)/2
		if matrix[midX][midY] == target {
			return true
		} else if matrix[midX][midY] < target {
			return helper(midX+1, y0, x1, y1) || helper(x0, midY+1, midX, y1)
		} else {
			return helper(x0, y0, midX-1, y1) || helper(midX, y0, x1, midY-1)
		}
	}
	return helper(0, 0, len(matrix)-1, len(matrix[0])-1)
}
