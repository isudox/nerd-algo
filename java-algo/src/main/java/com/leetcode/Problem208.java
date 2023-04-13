package com.leetcode;

/**
 * 208. Implement Trie (Prefix Tree)
 * https://leetcode.com/problems/implement-trie-prefix-tree/
 */
public class Problem208 {

    private static class Trie {

        private Trie[] children = new Trie[26];
        private boolean endpoint = false;

        /** Initialize your data structure here. */
        public Trie() {
        }

        /** Inserts a word into the trie. */
        public void insert(String word) {
            Trie cur = this;
            for (int i = 0; i < word.length(); i++) {
                int index = word.charAt(i) - 'a';
                if (cur.children[index] == null) {
                    cur.children[index] = new Trie();
                }
                cur = cur.children[index];
            }
            cur.endpoint = true;
        }

        /** Returns if the word is in the trie. */
        public boolean search(String word) {
            Trie cur = this;
            for (int i = 0; i < word.length(); i++) {
                int index = word.charAt(i) - 'a';
                if (cur.children[index] == null) {
                    return false;
                }
                cur = cur.children[index];
            }
            return cur.endpoint;
        }

        /** Returns if there is any word in the trie that starts with the given prefix. */
        public boolean startsWith(String prefix) {
            Trie cur = this;
            for (int i = 0; i < prefix.length(); i++) {
                int index = prefix.charAt(i) - 'a';
                if (cur.children[index] == null)
                    return false;
                cur = cur.children[index];
            }
            return true;
        }
    }

}
