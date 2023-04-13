# Trie Tree Node
from typing import Optional


class TrieNode:
    def __init__(self, char: Optional[str] = None):
        self.char = char
        self.children = []
        self.counter = 0
        self.end = False

    def add(self, word: str):
        node = self
        for char in word:
            found_in_children = False
            for child in node.children:
                if child.char == char:
                    found_in_children = True
                    child.counter += 1
                    node = child
                    break
            if not found_in_children:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.end = True
