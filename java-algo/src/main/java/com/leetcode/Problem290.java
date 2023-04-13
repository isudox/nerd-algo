package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 290. Word Pattern
 * https://leetcode.com/problems/word-pattern/
 */
public class Problem290 {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (pattern.length() != words.length) {
            return false;
        }
        Map<String, Character> map0 = new HashMap<>();
        Map<Character, String> map1 = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            Character ch = pattern.charAt(i);
            if (map0.containsKey(word) && map0.get(word) != ch) {
                return false;
            }
            if (map1.containsKey(ch) && !map1.get(ch).equals(word)) {
                return false;
            }
            map0.put(word, ch);
            map1.put(ch, word);
        }
        return true;
    }
}
