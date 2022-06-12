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
            if (check(word, pattern)) {
                ans.add(word);
            }
        }
        return ans;
    }

    private boolean check(String word, String pattern) {
        if (word.length() != pattern.length()) {
            return false;
        }
        Map<Character, Character> map1 = new HashMap<>();
        Map<Character, Character> map2 = new HashMap<>();
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i), p = pattern.charAt(i);
            if (map1.containsKey(p)) {
                if (map1.get(p) != c) {
                    return false;
                }
            } else {
                map1.put(p, c);
            }
            if (map2.containsKey(c)) {
                if (map2.get(c) != p) {
                    return false;
                }
            } else {
                map2.put(c, p);
            }
        }
        return true;
    }
}
