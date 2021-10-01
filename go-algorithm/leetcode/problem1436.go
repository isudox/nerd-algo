package leetcode

// 1436. Destination City
// https://leetcode.com/problems/destination-city/
func destCity(paths [][]string) string {
	graph := make(map[string]string)
	for _, path := range paths {
		graph[path[0]] = path[1]
	}
	cur := paths[0][0]
	for graph[cur] != "" {
		cur = graph[cur]
	}
	return cur
}
