package com.leetcode;

/**
 * 387. First Unique Character in a String
 * https://leetcode.com/problems/first-unique-character-in-a-string/
 */
class Problem387 {
    public int firstUniqChar(String s) {
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < s.length(); i++) {
            if (counter[s.charAt(i) - 'a'] == 1) return i;
        }
        return -1;
    }
}
