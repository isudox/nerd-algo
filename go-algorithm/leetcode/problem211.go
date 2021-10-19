package leetcode

// 211. Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

type WordDictionary struct {
	root *TrieNode
}

func _() WordDictionary {
	return WordDictionary{&TrieNode{}}
}

func (d *WordDictionary) AddWord(word string) {
	d.root.Insert(word)
}

func (d *WordDictionary) Search(word string) bool {
	var dfs func(int, *TrieNode) bool
	dfs = func(i int, node *TrieNode) bool {
		if i == len(word) {
			return node.word == word
		}
		ch := word[i]
		if ch != '.' {
			child := node.children[ch-'a']
			if child != nil && dfs(i+1, child) {
				return true
			}
		} else {
			for _, child := range node.children {
				if child != nil && dfs(i+1, child) {
					return true
				}
			}
		}
		return false
	}
	return dfs(0, d.root)
}
