package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 890. Find and Replace Pattern
 * https://leetcode.com/problems/find-and-replace-pattern/
 */
public class Problem890 {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> ans = new ArrayList<>();
        for (String word : words) {
            if (check(word, pattern) && check(pattern, word)) {
                ans.add(word);
            }
        }
        return ans;
    }

    private boolean check(String word, String pattern) {
        if (word.length() != pattern.length()) {
            return false;
        }
        Map<Character, Character> map = new HashMap<>();
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i), p = pattern.charAt(i);
            if (map.containsKey(p)) {
                if (map.get(p) != c) {
                    return false;
                }
            } else {
                map.put(p, c);
            }
        }
        return true;
    }
}
