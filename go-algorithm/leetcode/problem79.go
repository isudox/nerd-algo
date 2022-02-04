package main

// 79. Word Search
// https://leetcode.com/problems/word-search/

func exist(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])
	var bfs func(x, y, z int, seen [][]bool) bool
	bfs = func(x, y, z int, seen [][]bool) bool {
		if board[x][y] != word[z] {
			return false
		}
		if z == len(word)-1 {
			return true
		}
		seen[x][y] = true
		for _, d := range [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}} {
			nx, ny := x+d[0], y+d[1]
			if 0 <= nx && nx < m && 0 <= ny && ny < n && !seen[nx][ny] {
				if bfs(nx, ny, z+1, seen) {
					return true
				}
			}
		}
		seen[x][y] = false
		return false
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			seen := make([][]bool, m)
			for i := 0; i < m; i++ {
				seen[i] = make([]bool, n)
			}
			if bfs(i, j, 0, seen) {
				return true
			}
		}
	}
	return false
}
