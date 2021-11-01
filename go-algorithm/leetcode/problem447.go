package main

func numberOfBoomerangs(points [][]int) int {
	n := len(points)
	dict := make(map[int]map[int]int)
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			dx := points[j][0] - points[i][0]
			dy := points[j][1] - points[i][1]
			dist := dx*dx + dy*dy
			if dict[dist] == nil {
				dict[dist] = map[int]int{}
			}
			dict[dist][i]++
			dict[dist][j]++
		}
	}
	ans := 0
	for _, mapper := range dict {
		for _, cnt := range mapper {
			ans += (cnt - 1) * cnt
		}
	}
	return ans
}
