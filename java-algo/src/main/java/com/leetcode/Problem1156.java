package com.leetcode;

/**
 * 1156. Swap For Longest Repeated Character Substring
 * https://leetcode.com/problems/swap-for-longest-repeated-character-substring
 */
public class Problem1156 {
    public int maxRepOpt1(String text) {
        int[] counter = new int[26];
        for (int i = 0; i < text.length(); i++) {
            counter[text.charAt(i) - 'a']++;
        }
        int ans = 0;
        for (int i = 0; i < text.length(); i++) {
            int j = i;
            if (j > 0 && text.charAt(j) == text.charAt(j - 1)) {
                continue;
            }
            while (j < text.length() && text.charAt(j) == text.charAt(i)) {
                j++;
            }
            int sz = j - i;
            if (sz < counter[text.charAt(i) - 'a'] && (j < text.length() || i > 0)) {
                ans = Math.max(ans, sz + 1);
            }
            int k = j + 1;
            while (k < text.length() && text.charAt(k) == text.charAt(i)) {
                k++;
            }
            ans = Math.max(ans, Math.min((k - i), counter[text.charAt(i) - 'a']));
        }
        return ans;
    }
}
