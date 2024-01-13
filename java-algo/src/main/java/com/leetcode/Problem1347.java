package com.leetcode;

/**
 * 1347. Minimum Number of Steps to Make Two Strings Anagram
 * https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
 */
public class Problem1347 {
    public int minSteps(String s, String t) {
        int[] arr = new int[26];
        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i) - 'a']++;
            arr[t.charAt(i) - 'a']--;
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (arr[i] > 0) {
                ans += arr[i];
            }
        }
        return ans;
    }
}
