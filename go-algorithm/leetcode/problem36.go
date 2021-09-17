package leetcode

/*
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
*/
func isValidSudoku(board [][]byte) bool {
	rows, cols, boxes := make([]map[byte]bool, 9), make([]map[byte]bool, 9), make([]map[byte]bool, 9)
	for i := 0; i < 9; i++ {
		rows[i] = make(map[byte]bool)
		cols[i] = make(map[byte]bool)
		boxes[i] = make(map[byte]bool)
	}
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			ch := board[i][j]
			if ch == '.' {
				continue
			}
			if rows[i][ch] {
				return false
			}
			rows[i][ch] = true
			if cols[j][ch] {
				return false
			}
			cols[j][ch] = true
			boxIndex := i/3 + (j/3)*3
			if boxes[boxIndex][ch] {
				return false
			}
			boxes[boxIndex][ch] = true
		}
	}
	return true
}
