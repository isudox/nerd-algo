package main

// 6. ZigZag Conversion
// https://leetcode.com/problems/zigzag-conversion/

/*
A
Y A
P
*/

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

func convert2(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	ans := ""
	n := len(s)
	step := (numRows - 1) * 2
	for i := 0; i < numRows; i++ {
		for pos := 0; pos < n+step; pos += step {
			if i == 0 || i == numRows-1 {
				x := pos + i
				if 0 <= x && x < n {
					ans += string(s[x])
				}
			} else {
				x, y := pos-i, pos+i
				if 0 <= x && x < n {
					ans += string(s[x])
				}
				if 0 <= y && y < n {
					ans += string(s[y])
				}
			}
		}
	}
	return ans
}
