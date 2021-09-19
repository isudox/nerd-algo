package main

type TrieNode struct {
	children [26]*TrieNode
	word     string
}

func (t *TrieNode) Insert(word string) {
	node := t
	for _, c := range word {
		c -= 'a'
		if node.children[c] == nil {
			node.children[c] = &TrieNode{}
		}
		node = node.children[c]
	}
	node.word = word
}

var dirs = []struct{ x, y int }{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func findWords(board [][]byte, words []string) []string {
	t := &TrieNode{}
	for _, word := range words {
		t.Insert(word)
	}
	m, n := len(board), len(board[0])
	seen := map[string]bool{}
	var dfs func(node *TrieNode, x, y int)
	dfs = func(node *TrieNode, x, y int) {
		c := board[x][y]
		node = node.children[c-'a']
		if node == nil {
			return
		}
		if node.word != "" {
			seen[node.word] = true
		}
		board[x][y] = '#'
		for _, d := range dirs {
			nx, ny := x+d.x, y+d.y
			if 0 <= nx && nx < m && 0 <= ny && ny < n && board[nx][ny] != '#' {
				dfs(node, nx, ny)
			}
		}
		board[x][y] = c
	}
	for i, row := range board {
		for j := range row {
			dfs(t, i, j)
		}
	}
	ans := make([]string, 0, len(seen))
	for s := range seen {
		ans = append(ans, s)
	}
	return ans
}
