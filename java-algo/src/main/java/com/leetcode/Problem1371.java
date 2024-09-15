package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1371. Find the Longest Substring Containing Vowels in Even Counts
 * https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
 */
public class Problem1371 {
    public int findTheLongestSubstring(String s) {
        int ans = 0, n = s.length();
        int[] presum = new int[n + 1]; // a-e-i-o-u -> bitmap
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'a') {
                presum[i + 1] = presum[i] ^ (1);
            } else if (c == 'e') {
                presum[i + 1] = presum[i] ^ (1 << 1);
            } else if (c == 'i') {
                presum[i + 1] = presum[i] ^ (1 << 2);
            } else if (c == 'o') {
                presum[i + 1] = presum[i] ^ (1 << 3);
            } else if (c == 'u') {
                presum[i + 1] = presum[i] ^ (1 << 4);
            } else {
                presum[i + 1] = presum[i];
            }
        }
        Map<Integer, Integer> memo = new HashMap<>();
        memo.put(0, 0);
        for (int i = 1; i <= n; i++) {
            int bits = presum[i];
            if (memo.containsKey(bits)) {
                ans = Math.max(ans, i - memo.get(bits));
            } else {
                memo.put(bits, i);
            }
        }
        return ans;
    }
}
