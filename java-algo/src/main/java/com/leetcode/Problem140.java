package com.leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * 140. Word Break II
 * https://leetcode.com/problems/word-break-ii/
 */
public class Problem140 {
    private String s;
    private Set<String> words = new HashSet<>();

    public List<String> wordBreak(String s, List<String> wordDict) {
        this.s = s;
        this.words = new HashSet<>(wordDict);
        List<String> ans = new ArrayList<>();
        backtrack(ans, new ArrayList<>(), "", 0);
        return ans;
    }

    private void backtrack(List<String> ans, List<String> group, String pre, int i) {
        if (i == s.length()) {
            if (pre.isEmpty()) {
                ans.add(trans(group));
            }
            return;
        }
        String cur = pre + s.charAt(i);
        if (words.contains(cur)) {
            // case1: store current word
            group.add(cur);
            backtrack(ans, group, "", i + 1);
            // case2: continue to expand current word
            group.remove(group.size() - 1);
            backtrack(ans, group, cur, i + 1);
        } else {
            // case3: continue to expand current word
            backtrack(ans, group, cur, i + 1);
        }
    }

    private String trans(List<String> group) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < group.size(); i++) {
            sb.append(group.get(i));
            if (i != group.size() - 1) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}
