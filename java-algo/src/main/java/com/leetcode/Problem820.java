package com.leetcode;

/**
 * 820. Short Encoding of Words
 * https://leetcode.com/problems/short-encoding-of-words/
 */
public class Problem820 {
    public int minimumLengthEncoding(String[] words) {
        return 0;
    }

    private static class TrieNode {
        TrieNode[] children;
        
        public TrieNode() {
            this.children = new TrieNode[27];
        }

        public void insert(String word) {
            TrieNode cur = this;
            for(int i = 0; i < word.length(); i++) {
                int x = word.charAt(i) - 'a';
                if (cur.children[x] == null) {
                    cur.children[x] = new TrieNode();
                }
                cur = cur.children[x];
            }
        }
    }
}

