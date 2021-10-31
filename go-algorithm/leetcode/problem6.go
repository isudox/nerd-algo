package leetcode

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	n := len(s)
	x := n / (2*numRows - 2)
	y := n % (2*numRows - 2)
	if y <= numRows {
		y = 1
	} else {
		y += 1 - numRows
	}
	cols := x*(numRows-1) + y
	matrix := make([][]string, numRows)
	for i := 0; i < numRows; i++ {
		matrix[i] = make([]string, cols)
	}
	i := 0
	j := 0
	down := true
	for _, c := range s {
		matrix[i][j] = string(c)
		if i == 0 {
			down = true
		} else if i == numRows-1 {
			down = false
		}
		if down {
			i++
		} else {
			i--
			j++
		}
	}
	ans := ""
	for row := 0; row < numRows; row++ {
		for col := 0; col < cols; col++ {
			if matrix[row][col] != "" {
				ans += matrix[row][col]
			}
		}
	}
	return ans
}
