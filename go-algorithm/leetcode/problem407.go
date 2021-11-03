package main

import "container/heap"

// 407. Trapping Rain Water II
// https://leetcode.com/problems/trapping-rain-water-ii/

func trapRainWater(heightMap [][]int) (ans int) {
	m, n := len(heightMap), len(heightMap[0])
	if m <= 2 || n <= 2 {
		return
	}

	vis := make([][]bool, m)
	for i := range vis {
		vis[i] = make([]bool, n)
	}
	h := &CellSlice{}
	for i, row := range heightMap {
		for j, v := range row {
			if i == 0 || i == m-1 || j == 0 || j == n-1 {
				heap.Push(h, Cell{v, i, j})
				vis[i][j] = true
			}
		}
	}
	max := func(a, b int) int {
		if b > a {
			return b
		}
		return a
	}
	dirs := []int{-1, 0, 1, 0, -1}
	for h.Len() > 0 {
		cur := heap.Pop(h).(Cell)
		for k := 0; k < 4; k++ {
			nx, ny := cur.x+dirs[k], cur.y+dirs[k+1]
			if 0 <= nx && nx < m && 0 <= ny && ny < n && !vis[nx][ny] {
				if heightMap[nx][ny] < cur.h {
					ans += cur.h - heightMap[nx][ny]
				}
				vis[nx][ny] = true
				heap.Push(h, Cell{max(heightMap[nx][ny], cur.h), nx, ny})
			}
		}
	}
	return
}

type Cell struct{ h, x, y int }
type CellSlice []Cell

func (h CellSlice) Len() int            { return len(h) }
func (h CellSlice) Less(i, j int) bool  { return h[i].h < h[j].h }
func (h CellSlice) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *CellSlice) Push(v interface{}) { *h = append(*h, v.(Cell)) }
func (h *CellSlice) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }
