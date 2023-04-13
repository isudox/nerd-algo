package main

// 130. Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

func solve(board [][]byte) {
	m, n := len(board), len(board[0])
	marks := make([][]bool, m)
	for i := 0; i < m; i++ {
		marks[i] = make([]bool, n)
	}
	var dfs func(x, y int)
	dfs = func(x, y int) {
		marks[x][y] = true
		dirs := []struct{ x, y int }{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		for _, p := range dirs {
			nx, ny := x+p.x, y+p.y
			if 0 < nx && nx < m-1 && 0 < ny && ny < n-1 && board[nx][ny] == 'O' && !marks[nx][ny] {
				dfs(nx, ny)
			}
		}
	}
	for i := 0; i < m; i++ {
		if i == 0 || i == m-1 {
			for j := 0; j < n; j++ {
				if board[i][j] == 'O' && !marks[i][j] {
					dfs(i, j)
				}
			}
		} else {
			for _, j := range []int{0, n - 1} {
				if board[i][j] == 'O' && !marks[i][j] {
					dfs(i, j)
				}
			}
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == 'O' && !marks[i][j] {
				board[i][j] = 'X'
			}
		}
	}
}
