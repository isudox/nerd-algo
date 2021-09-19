package main

func spiralOrder(matrix [][]int) []int {
	var ans []int
	if matrix == nil {
		return ans
	}
	m, n := len(matrix), len(matrix[0])
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	x, y, size := 0, 0, m*n
	dirs := [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	i := 0
	ans = append(ans, matrix[0][0])
	visited[0][0] = true
	cnt := 1
	for cnt < size {
		nx, ny := x + dirs[i][0], y + dirs[i][1]
		if 0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny] {
			x = nx
			y = ny
		} else {
			i = (i + 1) % 4
			x += dirs[i][0]
			y += dirs[i][1]
		}
		ans = append(ans, matrix[x][y])
		visited[x][y] = true
		cnt++
	}
	return ans
}
