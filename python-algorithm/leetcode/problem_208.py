"""208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
import collections


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode()
                node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = collections.defaultdict(TrieNode)
