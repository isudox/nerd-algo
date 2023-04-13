package main

import (
	"container/heap"
	"sort"
)

func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	n := len(capital)
	pairs := make([][2]int, n)
	for i := 0; i < n; i++ {
		pairs[i] = [2]int{capital[i], profits[i]}
	}
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i][0] < pairs[j][0]
	})
	store := &hp{}
	for pos := 0; k > 0; k-- {
		for pos < n && pairs[pos][0] <= w {
			heap.Push(store, pairs[pos][1])
			pos++
		}
		if store.Len() == 0 {
			break
		}
		w += heap.Pop(store).(int)
	}
	return w
}

type hp struct {
	sort.IntSlice
}

func (h hp) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}
