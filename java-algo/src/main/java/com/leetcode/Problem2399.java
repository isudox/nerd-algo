package com.leetcode;

import java.util.Arrays;

/**
 * 2399. Check Distances Between Same Letters
 * https://leetcode.com/problems/check-distances-between-same-letters/
 */
public class Problem2399 {
    public boolean checkDistances(String s, int[] distance) {
        int[] store = new int[26];
        Arrays.fill(store, -1);
        for (int i = 0; i < s.length(); i++) {
            int d = s.charAt(i) - 'a';
            if (store[d] >= 0) {
                if (i - store[d] - 1 != distance[d]) {
                    return false;
                }
            } else {
                store[d] = i;
            }
        }
        return true;
    }
}
