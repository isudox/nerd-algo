package leetcode

import (
	"bytes"
	"sort"
)

// 451. Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

func frequencySort(s string) string {
	counter := make(map[byte]int)
	for i := range s {
		counter[s[i]] += 1
	}
	type pair struct {
		ch  byte
		cnt int
	}
	pairs := make([]pair, 0, len(counter))
	for k, v := range counter {
		pairs = append(pairs, pair{k, v})
	}
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].cnt > pairs[j].cnt
	})
	ans := make([]byte, 0, len(s))
	for _, p := range pairs {
		ans = append(ans, bytes.Repeat([]byte{p.ch}, p.cnt)...)
	}
	return string(ans)
}
