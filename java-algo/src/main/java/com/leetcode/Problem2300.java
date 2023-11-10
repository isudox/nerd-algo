package com.leetcode;

import java.util.Arrays;

/**
 * 2300. Successful Pairs of Spells and Potions
 * https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
 */
public class Problem2300 {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length, m = potions.length;
        int[] ans = new int[n];
        Arrays.sort(potions);
        for (int i = 0; i < n; i++) {
            long x = success / spells[i] + (success % spells[i] > 0 ? 1 : 0);
            if (potions[m - 1] < x) {
                continue;
            }
            int lo = 0, hi = potions.length - 1, mid;
            while (lo < hi) {
                mid = (lo + hi) >> 1;
                if (potions[mid] < x) {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            ans[i] = m - lo;
        }
        return ans;
    }
}
