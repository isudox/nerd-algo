package com.leetcode;

/**
 * 1160. Find Words That Can Be Formed by Characters
 */
public class Problem1160 {
    public int countCharacters(String[] words, String chars) {
        int[] store = new int[26];
        for (char c : chars.toCharArray()) {
            store[c - 'a']++;
        }
        int ans = 0;
        for (String word : words) {
            boolean ok = true;
            int[] cnt = new int[26];
            for (char c : word.toCharArray()) {
                if (++cnt[c - 'a'] > store[c - 'a']) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                ans += word.length();
            }
        }
        return ans;
    }
}
