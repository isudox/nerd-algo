package com.leetcode;

/**
 * 211. Design Add and Search Words Data Structure
 * https://leetcode.com/problems/design-add-and-search-words-data-structure/
 */
public class Problem211 {
    static class WordDictionary {
        private Trie t;

        public WordDictionary() {
            this.t = new Trie();
        }

        public void addWord(String word) {
            Trie cur = t;
            for (int i = 0; i < word.length(); i++) {
                int c = word.charAt(i) - 'a';
                if (cur.children[c] == null) {
                    cur.children[c] = new Trie();
                }
                cur = cur.children[c];
            }
            cur.end = true;
        }

        public boolean search(String word) {
            return t.search(word);
        }
    }

    static class Trie {
        private Trie[] children = new Trie[26];
        private boolean end = false;

        public Trie() {
        }

        public boolean search(String word) {
            Trie t = this;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (c == '.') {
                    for (Trie next : t.children) {
                        if (next != null && next.search(word.substring(i + 1))) {
                            return true;
                        }
                    }
                    return false;
                }
                if (t.children[c - 'a'] == null) {
                    return false;
                }
                t = t.children[c - 'a'];
            }
            return t.end;
        }
    }

    public static void main(String[] args) {
        Problem211.WordDictionary wordDictionary = new Problem211.WordDictionary();
        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        System.out.println(wordDictionary.search("b.."));
    }
}
