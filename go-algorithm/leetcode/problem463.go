package leetcode

// 463. Island Perimeter
// https://leetcode.com/problems/island-perimeter/
func islandPerimeter(grid [][]int) int {
	dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	ans := 0
	m, n := len(grid), len(grid[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				for _, d := range dirs {
					nx, ny := i+d[0], j+d[1]
					if nx < 0 || nx == m || ny < 0 || ny == n || grid[nx][ny] == 0 {
						ans++
					}
				}
			}
		}
	}
	return ans
}
