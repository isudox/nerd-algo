package leetcode

// 463. Island Perimeter
// https://leetcode.com/problems/island-perimeter/
func islandPerimeter(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	seen := make([][]bool, m)
	for i := 0; i < m; i++ {
		seen[i] = make([]bool, n)
	}
	ans := 0
	dirs := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	var bfs func(x, y int)
	bfs = func(x, y int) {
		if seen[x][y] {
			return
		}
		seen[x][y] = true
		for _, dir := range dirs {
			nx, ny := x+dir[0], y+dir[1]
			if grid[x][y] == 1 {
				if (nx < 0 || nx == m || ny < 0 || ny == n) || grid[nx][ny] == 0 {
					ans++
				}
			}
			if 0 <= nx && nx < m && 0 <= ny && ny < n && !seen[nx][ny] {
				bfs(nx, ny)
			}
		}
	}
	bfs(0, 0)
	return ans
}
