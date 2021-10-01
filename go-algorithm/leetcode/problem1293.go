package leetcode

import "math"

// 1293. Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
func shortestPath(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	dirs := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	var dfs func(x, y, z int) int
	dfs = func(x, y, z int) int {
		if x == m-1 && y == n-1 {
			return 0
		}
		ret := math.MaxInt8
		if grid[x][y] == 0 {
			visited[x][y] = true
			for _, dir := range dirs {
				nx, ny := x+dir[0], y+dir[1]
				if 0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny] {
					ret = min(ret, dfs(nx, ny, z)+1)
				}
			}
		} else {
			if z == 0 {
				return math.MaxInt8
			}
			visited[x][y] = true
			for _, dir := range dirs {
				nx, ny := x+dir[0], y+dir[1]
				if 0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny] {
					ret = min(ret, dfs(nx, ny, z-1)+1)
				}
			}
		}
		visited[x][y] = false
		return ret
	}
	result := dfs(0, 0, k)
	if result == math.MaxInt8 {
		return -1
	}
	return result
}
