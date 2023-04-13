package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 386. Lexicographical Numbers
 * https://leetcode.com/problems/lexicographical-numbers/
 */
public class Problem386 {
    public List<Integer> lexicalOrder(int n) {
        Trie t = new Trie();
        for (int i = 1; i <= n; i++) {
            t.insert(i);
        }
        List<Integer> ans = new ArrayList<>();
        dfs(t, 0, ans);
        return ans;
    }

    private static class Trie {
        private final Trie[] children = new Trie[10];
        private boolean end = false;

        public Trie() {
        }

        public void insert(int num) {
            String str = String.valueOf(num);
            Trie cur = this;
            for (char ch : str.toCharArray()) {
                int i = ch - '0';
                if (cur.children[i] == null) {
                    cur.children[i] = new Trie();
                }
                cur = cur.children[i];
            }
            cur.end = true;
        }
    }

    private void dfs(Trie trie, int num, List<Integer> list) {
        if (trie == null) {
            return;
        }
        for (int i = 0; i < 10; i++) {
            Trie cur = trie.children[i];
            if (cur == null) {
                continue;
            }
            if (cur.end) {
                list.add(num * 10 + i);
            }
            dfs(cur, num * 10 + i, list);
        }
    }
}
