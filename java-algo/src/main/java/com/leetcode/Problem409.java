package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 409. Longest Palindrome
 * https://leetcode.com/problems/longest-palindrome/
 */
public class Problem409 {
    public int longestPalindrome(String s) {
        Map<Character, Integer> cnts = new HashMap<>();
        for (char c : s.toCharArray()) {
            cnts.put(c, cnts.getOrDefault(c, 0) + 1);
        }
        int ans = 0, maxOdd = 0;
        for (int cnt : cnts.values()) {
            if (cnt % 2 == 0) {
                ans += cnt;
            } else {
                ans += cnt - 1;
                maxOdd = Math.max(maxOdd, cnt);
            }
        }
        return maxOdd == 0 ? ans : ans + 1;
    }
}
