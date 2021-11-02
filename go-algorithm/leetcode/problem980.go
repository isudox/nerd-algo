package main

// 980. Unique Paths III
// https://leetcode.com/problems/unique-paths-iii

func uniquePathsIII(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	ans := 0
	zeroCnt := 0
	startX, startY := 0, 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				zeroCnt++
			} else if grid[i][j] == 1 {
				startX = i
				startY = j
			}
		}
	}
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	var backtrack func(x, y, zero int)
	backtrack = func(x, y, zero int) {
		for _, d := range []struct{ x, y int }{{0, 1}, {0, -1}, {1, 0}, {-1, 0}} {
			nx, ny := x+d.x, y+d.y
			if 0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny] && grid[nx][ny] != -1 {
				if grid[nx][ny] == 0 {
					visited[nx][ny] = true
					backtrack(nx, ny, zero+1)
					visited[nx][ny] = false
				} else if zero == zeroCnt {
					ans++
				}
			}
		}
	}
	visited[startX][startY] = true
	backtrack(startX, startY, 0)
	return ans
}
