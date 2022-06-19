package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1268. Search Suggestions System
 * https://leetcode.com/problems/search-suggestions-system/
 */
public class Problem1268 {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        TrieNode trie = new TrieNode();
        for (String product : products) {
            trie.add(product);
        }
        List<List<String>> ans = new ArrayList<>();
        String prefix = "";
        for (int i = 0; i < searchWord.length(); i++) {
            prefix += searchWord.charAt(i);
            ans.add(helper(trie, prefix));
        }
        return ans;
    }

    private List<String> helper(TrieNode trie, String prefix) {
        TrieNode cur = trie;
        List<String> list = new ArrayList<>();
        for (int i = 0; i < prefix.length(); i++) {
            char ch = prefix.charAt(i);
            if (cur.children[ch - 'a'] == null) {
                return list;
            }
            cur = cur.children[ch - 'a'];
        }
        dfs(cur, prefix, list);
        return list;
    }

    private void dfs(TrieNode trie, String word, List<String> list) {
        if (list.size() == 3) {
            return;
        }
        if (trie.end) {
            list.add(word);
        }
        for (char ch = 'a'; ch <= 'z'; ch++) {
            if (trie.children[ch - 'a'] != null) {
                dfs(trie.children[ch - 'a'], word + ch, list);
            }
        }
    }

    private static class TrieNode {
        TrieNode[] children;
        boolean end;

        public TrieNode() {
            this.children = new TrieNode[26];
        }

        public void add(String word) {
            TrieNode cur = this;
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);
                if (cur.children[ch - 'a'] == null) {
                    cur.children[ch - 'a'] = new TrieNode();
                }
                cur = cur.children[ch - 'a'];
            }
            cur.end = true;
        }
    }
}
