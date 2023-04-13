package com.leetcode;

import java.util.*;

/**
 * 1048. Longest String Chain
 * https://leetcode.com/problems/longest-string-chain/
 */
public class Problem1048 {
    public int longestStrChain(String[] words) {
        int ans = 0;
        Set<String> set = new HashSet<>(Arrays.asList(words));
        Map<String, Integer> memo = new HashMap<>();
        for (String word : set) {
            ans = Math.max(ans, dfs(set, word, memo));
        }
        return ans;
    }

    private int dfs(Set<String> set, String word, Map<String, Integer> memo) {
        if (memo.containsKey(word)) {
            return memo.get(word);
        }
        int ret = 1;
        for (int i = 0; i < word.length(); i++) {
            String next = word.substring(0, i) + word.substring(i + 1);
            if (set.contains(next)) {
                ret = Math.max(ret, dfs(set, next, memo) + 1);
            }
        }
        memo.put(word, ret);
        return ret;
    }
}
