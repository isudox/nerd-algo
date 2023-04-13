package main

// 488. Zuma Game
// https://leetcode.com/problems/zuma-game/

type state struct {
	board string
	hand  [5]int
}

func findMinStep(board string, hand string) int {
	cache := map[string]string{}
	COLORS := "RYBGW"

	var clean func(b string) string
	clean = func(board string) string {
		if v, ok := cache[board]; ok {
			return v
		}
		res := board
		for i, j := 0, 0; i < len(board); {
			for j < len(board) && board[i] == board[j] {
				j += 1
			}
			if j-i > 2 {
				res = clean(board[:i] + board[j:])
				cache[board] = res
				return res
			}
			i = j
		}
		cache[board] = res
		return res
	}

	count := func(hand string) [5]int {
		res := [5]int{}
		for i := 0; i < len(hand); i++ {
			for j, c := range COLORS {
				if hand[i] == byte(c) {
					res[j]++
					break
				}
			}
		}
		return res
	}

	queue := make([]state, 0, 6)
	init := state{board, count(hand)}
	queue = append(queue, init)
	visited := map[state]int{}
	visited[init] = 0
	for len(queue) > 0 {
		curState := queue[0]
		cur_board, cur_hand := curState.board, curState.hand
		if len(cur_board) == 0 {
			return visited[curState]
		}
		queue = queue[1:]
		for i := 0; i <= len(cur_board); i++ {
			for j, r := range COLORS {
				if cur_hand[j] > 0 {
					c := byte(r)
					// 第 1 个剪枝条件: 只在连续相同颜色的球的开头位置插入新球(在它前面插入过了，不需要再插入，意义相同)
					if i > 0 && cur_board[i-1] == c {
						continue
					}
					/**
					 *  第 2 个剪枝条件: 只在以下两种情况放置新球
					 *  - 第 1 种情况 : 当前后颜色相同且与当前颜色不同时候放置球
					 *  - 第 2 种情况 : 当前球颜色与后面的球的颜色相同
					 */
					choose := false
					if 0 < i && i < len(cur_board) && cur_board[i-1] == cur_board[i] && cur_board[i-1] != c {
						choose = true
					}
					if i < len(cur_board) && cur_board[i] == c {
						choose = true
					}

					if choose {
						nxt := [5]int{}
						for k, _ := range COLORS {
							nxt[k] = cur_hand[k]
						}
						nxt[j] -= 1

						nextState := state{clean(cur_board[:i] + string(c) + cur_board[i:]), nxt}
						if _, ok := visited[nextState]; !ok {
							queue = append(queue, nextState)
							visited[nextState] = visited[curState] + 1
						}
					}
				}
			}
		}
	}
	return -1
}
