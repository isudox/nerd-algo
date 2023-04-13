package main

// package main 208. Implement Trie (Prefix Tree)
// https://leetcode.com/problems/implement-trie-prefix-tree/

type Trie struct {
	children [26]*Trie
	isEnd    bool
}

func _() Trie {
	return Trie{}
}

func (t *Trie) Insert(word string) {
	node := t
	for _, c := range word {
		c -= 'a'
		if node.children[c] == nil {
			node.children[c] = &Trie{}
		}
		node = node.children[c]
	}
	node.isEnd = true
}

func (t *Trie) SearchPrefix(prefix string) *Trie {
	node := t
	for _, c := range prefix {
		c -= 'a'
		if node.children[c] == nil {
			return nil
		}
		node = node.children[c]
	}
	return node
}

func (t *Trie) Search(word string) bool {
	node := t.SearchPrefix(word)
	return node != nil && node.isEnd
}

func (t *Trie) StartsWith(prefix string) bool {
	return t.SearchPrefix(prefix) != nil
}
