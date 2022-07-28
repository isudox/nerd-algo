package com.leetcode;

/**
 * 242. Valid Anagram
 */
public class Problem242 {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        if (s.equals(t)) return true;
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a'] += 1;
            counter[t.charAt(i) - 'a'] -= 1;
        }
        for (int count : counter) {
            if (count != 0) return false;
        }
        return true;
    }
}
